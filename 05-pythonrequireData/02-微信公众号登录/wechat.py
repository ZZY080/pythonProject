import hashlib
import urllib.request as urllib2
from flask import Flask, request, abort, render_template
from flask_cors import  CORS
import requests
#  把字符串转换为xml
import xmltodict
import time
import json
import redis
app = Flask(__name__)
CORS(app)
# 获取redis数据库连接
r= redis.StrictRedis(host="127.0.0.1",port=6379,db=0)


FromUserName=None
# 微信的token令牌
WECHAT_TOKEN = "6666"
WECHAT_APPID= "wx189cfe8f606ae51e"
WECHAT_APPSECRET="0399108fdd23d5a61db2bcfbe90d3f79"

# 供微信用户使用的api
@app.route("/wx",methods=['GET',"POST"])
def wechat():
    """对接微信公众号服务器"""
    # 接收微信服务器发送的参数
    signature = request.args.get("signature")
    timestamp = request.args.get("timestamp")
    nonce = request.args.get("nonce")

    # 校验参数
    if not all([signature,timestamp,nonce]):
        abort(400)
    # 按照微信流程进行计算签名
    li =[WECHAT_TOKEN,timestamp,nonce]
    # 排序
    li.sort()
    # 拼接字符串
    tmp_str = "".join(li)
    # 进行sha1加密，得到正确的签名值
    sign = hashlib.sha1(tmp_str.encode()).hexdigest()
    # 将自己计算的签名与请求的签名参数进行对比，如果相同，则证明请求来自微信服务器
    if signature != sign:
        # 表示请求不是微信发送的
        abort(403)
    else:
        # 表示时微信发送的请求
        if request.method == "GET":
            # 表示是第一次接入微信服务器的验证
            echostr = request.args.get("echostr")
            if not echostr:
                abort(400)
            return echostr
        elif request.method == "POST":
            # 表示微信服务器转发消息过来
            xml_str = request.data
            if not xml_str:
                abort(400)
            # 对xml字符串进行解析
            xml_dict = xmltodict.parse(xml_str)
            xml_dict = xml_dict.get("xml")

            # 提取消息类型
            msg_type = xml_dict.get("MsgType")
            global FromUserName
            FromUserName = xml_dict.get("FromUserName")
            if msg_type=="text":
                #  表示发送的是文本消息
                #  构造返回值，经由微信服务器回复给用户的消息内容
                resp_dict = {
                   "xml":{
                       "ToUserName": xml_dict.get("FromUserName"),
                       "FromUserName": xml_dict.get("ToUserName"),
                       "CreateTime": int(time.time()),
                       "MsgType": "text",
                       "Content": xml_dict.get("Content")
                    }
                }
            elif msg_type=="event":
                #  表示发送的是文本消息
                #  构造返回值，经由微信服务器回复给用户的消息内容 当为订阅事件时
                Event = xml_dict.get("Event")
                if Event == "subscribe":
                    resp_dict = {
                        "xml": {
                            "ToUserName": xml_dict.get("FromUserName"),
                            "FromUserName": xml_dict.get("ToUserName"),
                            "CreateTime": int(time.time()),
                            "MsgType": "text",
                            "Content": "感谢您的关注"
                        }
                    }
                    r.set(name=FromUserName,value="1")


                elif Event == "unsubscribe":
                    resp_dict = {
                        "xml": {
                            "ToUserName": xml_dict.get("FromUserName"),
                            "FromUserName": xml_dict.get("ToUserName"),
                            "CreateTime": int(time.time()),
                            "MsgType": "text",
                            "Content": "如有打扰请多多包涵"
                        }
                    }
                    r.set(name=FromUserName,value="0")
            else:
                #  表示发送的是文本消息
                #  构造返回值，经由微信服务器回复给用户的消息内容
                resp_dict = {
                   "xml":{
                       "ToUserName": xml_dict.get("FromUserName"),
                       "FromUserName": xml_dict.get("ToUserName"),
                       "CreateTime": int(time.time()),
                       "MsgType": "text",
                       "Content": "kenny love you"
                   }
                }
            # 将字典转换为xml字符串
            resp_xml_str = xmltodict.unparse(resp_dict)
            # 返回消息数据给微信服务器
            return resp_xml_str

# 登录接口
@app.route("/wx/login",methods=["GET"])
def login():
    loginmsg={}

    loginmsg["isSubscribe"]= r.get(FromUserName).decode() if r.get(FromUserName) else 0
    if loginmsg["isSubscribe"]=="1":
        loginmsg['messages']="登录成功"
        loginmsg['userId']=FromUserName
    elif loginmsg["isSubscribe"]=="0":
        loginmsg['messages']="退出登录"
        loginmsg['userId']=FromUserName

    return json.dumps(loginmsg)



@app.route("/wx/index")
def index():
    """让用户通过微信访问的网页页面视图"""
    # 从微信服务器中拿取用户的资料
    # 1.拿取code参数
    code = request.args.get("code")
    print(code)
    print('--------')
    if not code:
        return "获取code参数失败"
    # 2.向微信服务器发送http请求，获取access_token

    url = "https://api.weixin.qq.com/sns/oauth2/access_token?appid=%s&secret=%s&code=%s&grant_type=authorization_code"%(WECHAT_APPID,WECHAT_APPSECRET,code)
    # 使用urlib2的urlopen方法发送请求
    # 如果只传网址url参数,则默认使用http的get请求方式,返回响应对象
    response =urllib2.urlopen(url)
    # 获取响应体数据，微信返回的json数据
    json_str = response.read()
    resp_dict = json.loads(json_str)

    # 提取access_token
    if "errcode" in resp_dict:
        return "获取access_token失败"
    access_token = resp_dict.get("access_token")
    # 获取用户编号
    open_id = resp_dict.get("openid")

    # 3. 向服务器发送http请求，获取用户数据
    url = "https://api.weixin.qq.com/sns/userinfo?access_token=%s&openid=%s&lang=zh_CN"%(access_token,open_id)
    response = urllib2.urlopen(url)
    # 读取微信传回的json的响应体数据
    user_json_str = response.read()
    user_dict_data = json.loads(user_json_str)
    if "errcode" in user_dict_data:
        return " 获取用户信息失败"
    else:
        # 将用户的资料数据填充到页面
        return render_template("index.html",user_dict_data)

@app.route("/wx/getQrCode",methods=['GET',"POST"])
def getQrcode():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"%(WECHAT_APPID,WECHAT_APPSECRET)
    response= urllib2.urlopen(url)
    json_str = response.read()
    data_dict = json.loads(json_str)
    access_token= data_dict.get("access_token")
    QrCodeUrl="https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s"%(access_token)

    print(access_token)
    return "hello"




if __name__ == "__main__":
    app.run(port=8080,debug=True)


#  http://dftpgb.natappfree.cc/wx/index
#  https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx189cfe8f606ae51e&redirect_uri=http%3A//amz7b2.natappfree.cc/wx/index&response_type=code&scope=snsapi_userinfo&state=123#wechat_redirect
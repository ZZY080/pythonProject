from flask import  Flask
from flask_cors import  CORS
import  requests
import  json
import time
app=Flask(__name__)
CORS(app)
@app.route("/data",methods=['POST','GET'])
def data():
    url="https://geo.datav.aliyun.com/areas_v3/bound/geojson?code=500000_full"
    content=requests.get(url=url).text
    return content

@app.route("/newadd",methods=['POST','GET'])
def newadd():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url = "https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=1671770092303"
    content = requests.get(url=url, headers=headers).text

    content_dic = json.loads(content).get("data").get("areaTree")[2].get("children")[9].get("children")

    total_data = []
    rename = ["酉阳县", "秀山县", "彭水县", "石柱县"]
    for item in content_dic:
        data_dic = {}
        name = item.get('name')
        value = item.get("total").get("confirm", 0)
        if name in rename:
            if name in rename[:2]:
                data_dic["name"] = name[0:2] + '土家族苗族自治县'
            elif name in rename[2]:
                data_dic["name"] = name[0:2] + '苗族土家族自治县'
            elif name in rename[3]:
                data_dic["name"] = name[0:2] + '土家族自治县'
        else:
            data_dic["name"] = name
        data_dic["value"] = value
        total_data.append(data_dic)
    total_data=json.dumps(total_data)
    return total_data

@app.route("/news",methods=['POST','GET'])
def news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    url = 'https://events.baidu.com/api/vein?platform=pc&page_size=10&order_type=0&page_from=1&tag=%E9%98%B2%E7%96%AB%E6%94%BF%E7%AD%96&record_id=20236&query=%E7%96%AB%E6%83%85'  # 定义要访问的地址
    # 使用requests发起请求 获取数据
    content = requests.get(url, headers=headers).text

    # 将数据转成字典
    content_dic = json.loads(content).get("data").get("nodes")

    news_data = []
    # 遍历所有字典数据 处理成我们想要的数据
    for item in content_dic:
        data_dic = {}
        timeArray = time.localtime(item.get("publish_time"))
        data_dic["publish_time"] = time.strftime("%Y-%m-%d", timeArray)
        data_dic["title"] = item.get("title")
        data_dic["url"] = item.get("url")
        news_data.append(data_dic)
    news_data=json.dumps(news_data)
    return  news_data

@app.route("/dataline",methods=['POST','GET'])
def dataline():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    url1 = "https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode=500000&t=1671804155290"
    url2 = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=334373233368'
    content1 = requests.get(url=url1, headers=headers).text
    content2 = requests.get(url2, headers=headers).text
    content_dic1 = json.loads(content1).get("data").get("list")
    content_dic2 = json.loads(content2).get("data").get("areaTree")[2].get("children")[9].get("today")
    # url1 的数据处理
    time = []
    confirm = []
    heal = []
    dead = []
    for item in content_dic1:
        time.append(item.get("date", "暂无日期"))
        confirm.append(item.get("today").get("confirm", "暂无数据"))
        heal.append(item.get("today").get("heal", "暂无数据"))
        dead.append(item.get("today").get("dead", "暂无数据"))
    data_line = {}
    data_line['time'] = time
    data_line['heal'] = heal
    data_line['confirm'] = confirm
    data_line['dead'] = dead

    # url2 数据处理
    data_add = {}
    data_add['confirmtoday'] = content_dic2.get("confirm")
    data_add['healtoday'] = content_dic2.get("heal")
    data_add['deadtoday'] = content_dic2.get("dead")
    total_data=[]
    total_data.append(data_line)
    total_data.append(data_add)
    total_data=json.dumps(total_data)

    return total_data


if __name__=='__main__':
    app.run()
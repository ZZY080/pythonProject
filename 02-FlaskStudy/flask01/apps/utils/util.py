import random

from flask import session
from qiniu import Auth, put_file, etag, put_data, BucketManager
import qiniu.config

from apps.article.models import Article_type
from apps.user.models import User
from  apps.user.smssend import SmsSendAPIDemo

def upload_qiniu(filestorage):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'QjKh9hTtXduWAMp4nE6Sko1EOvxksknOv0R1vT-Z'
    secret_key = '6Lq3VShSWSO0Cw-u7SR9cKd2t2ob9A2yckAYUpkS'
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = 'flaskblog123'
    # 上传后保存的文件名
    filename = filestorage.filename
    ran = random.randint(1, 1000)
    suffix = filename.rsplit('.')[-1]
    key = filename.rsplit('.')[0] + '_' + str(ran) + '.' + suffix
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 要上传文件的本地路径
    # localfile = './sync/bbb.jpg'
    # ret, info = put_file(token, key, localfile)
    ret, info = put_data(token, key, filestorage.read())
    return ret, info

def delete_qiniu(filename):
    # 需要填写你的 Access Key 和 Secret Key
    access_key = 'QjKh9hTtXduWAMp4nE6Sko1EOvxksknOv0R1vT-Z'
    secret_key = '6Lq3VShSWSO0Cw-u7SR9cKd2t2ob9A2yckAYUpkS'
    # 初始化Auth状态
    q = Auth(access_key, secret_key)
    # 初始化BucketManager
    bucket = BucketManager(q)
    # 你要测试的空间， 并且这个key在你空间中存在
    bucket_name = 'flaskblog123'
    key = filename
    # 删除bucket_name 中的文件 key
    ret, info = bucket.delete(bucket_name, key)
    return  info

def user_type():
    # 获取文章分类
    types = Article_type.query.all()
    # 登录用户
    user = None
    user_id = session.get('uid', None)
    if user_id:
        user = User.query.get(user_id)
    return user, types

# 发送短信
def send_messages(phone):
    """示例代码入口"""
    SECRET_ID = "aaf5de54985d8cc81fbc9ad4386fe63e"  # 产品密钥ID，产品标识
    SECRET_KEY = "2d743671588805e97bb913a5a0fb1b08"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "42a3d7ba3e404ac38deff746cbd3c0ca"  # 业务ID，易盾根据产品业务特点分配
    api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)
    code=""
    for i in range(4):
        ran=random.randint(0,9)
        code+=str(ran)
    params = {
        "mobile": phone,
        "templateId": "10084",
        "paramType": "json",
        "params":{"code":code}
    }
    ret = api.send(params)
    return ret,code

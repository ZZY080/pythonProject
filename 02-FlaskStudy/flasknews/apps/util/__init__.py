# 发送短信
import random

from apps.util.smssend import SmsSendAPIDemo


def send_messages(phone):
    """示例代码入口"""
    # SECRET_ID = "aaf5de54985d8cc81fbc9ad4386fe63e"  # 产品密钥ID，产品标识
    # SECRET_KEY = "2d743671588805e97bb913a5a0fb1b08"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    # BUSINESS_ID = "42a3d7ba3e404ac38deff746cbd3c0ca"  # 业务ID，易盾根据产品业务特点分配
    # api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)
    SECRET_ID = "dcc535cbfaefa2a24c1e6610035b6586"  # 产品密钥ID，产品标识
    SECRET_KEY = "d28f0ec3bf468baa7a16c16c9474889e"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "748c53c3a363412fa963ed3c1b795c65"  # 业务ID，易盾根据产品业务特点分配
    api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)
    code=""
    for i in range(4):
        ran=random.randint(0,9)
        code+=str(ran)
    params = {
        "mobile": phone,
        "templateId": "11732",
        "paramType": "json",
        "params":{"code":code}
    }
    ret = api.send(params)
    return ret,code

def login_required(func):
    def wrapper(*args,**kwargs):
        pass
        return  func(*args,**kwargs)

    return  wrapper
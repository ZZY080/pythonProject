import requests
import pandas as pd
import time
import json
pd.options.display.max_rows=500
# 伪造请求头进行反爬
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
url = 'https://static.ws.126.net/163/f2e/news/virus_province/static/chongqing.json'   # 定义要访问的地址
r = requests.get(url, headers=headers)  # 使用requests发起请求
# print(r.status_code)  # 查看请求状态
data_json = json.loads(r.text)
data_json.keys()
data = data_json['features'] # 取出json中的数据
#data.keys()
for i in range(len(data)): # 遍历查看
    if i == 37:
        break
# 获取id、type
info = pd.DataFrame(data)[['type','id']]
info.head()
# 获取properties中的数据
properties_data = pd.DataFrame([province['properties'] for province in data])
properties_data.head()

# 将提取数据的方法封装为函数
def get_data(data,info_list):
    info = pd.DataFrame(data)[info_list] # 主要信息
    properties_data = pd.DataFrame([i['properties'] for i in data ]) # 生成properties的数据

    return pd.concat([info,properties_data],axis=1) # info、today和total横向合并最终得到汇总的数据
province = get_data(data,['type','id'])
def save_data(data,name): # 定义保存数据方法
    file_name = name+'_'+time.strftime('%Y_%m_%d',time.localtime(time.time()))+'.csv'
    data.to_csv(file_name,index=None,encoding='utf_8_sig')
    print(file_name+' 保存成功！')
time.strftime('%Y_%m_%d',time.localtime(time.time()))
save_data(province,'province')
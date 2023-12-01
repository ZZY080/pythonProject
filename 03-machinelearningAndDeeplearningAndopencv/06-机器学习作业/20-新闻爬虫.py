#新闻爬虫
import requests
import time
import json

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

url = 'https://events.baidu.com/api/vein?platform=pc&page_size=10&order_type=0&page_from=1&tag=%E9%98%B2%E7%96%AB%E6%94%BF%E7%AD%96&record_id=20236&query=%E7%96%AB%E6%83%85'   # 定义要访问的地址
# 使用requests发起请求 获取数据
content= requests.get(url, headers=headers).text

# 将数据转成字典
content_dic=json.loads(content).get("data").get("nodes")

news_data=[]
# 遍历所有字典数据 处理成我们想要的数据
for item in content_dic:
    data_dic={}
    timeArray=time.localtime(item.get("publish_time"))
    data_dic["publish_time"]=time.strftime("%Y-%m-%d",timeArray)
    data_dic["title"]=item.get("title")
    data_dic["url"]=item.get("url")
    news_data.append(data_dic)
print(news_data)




import  requests
import json
url='https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=334373233368'
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
content=requests.get(url,headers=headers).text;
content_dic=json.loads(content).get("data").get("areaTree")[2].get("children")[9].get("today")
data_add={}
data_add['confirm']=content_dic.get("confirm")
data_add['heal']=content_dic.get("heal")
data_add['dead']=content_dic.get("dead")

data_json=json.dumps(data_add)
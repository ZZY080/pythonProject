import requests
import json
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
url="https://c.m.163.com/ug/api/wuhan/app/data/list-by-area-code?areaCode=500000&t=1671804155290"
content=requests.get(url=url,headers=headers).text
content_dic=json.loads(content).get("data").get("list")
time=[]
confirm=[]
heal=[]
dead=[]
for item in content_dic:
    time.append(item.get("date","暂无日期"))
    confirm.append(item.get("today").get("confirm","暂无数据"))
    heal.append(item.get("today").get("heal","暂无数据"))
    dead.append(item.get("today").get("dead","暂无数据"))
data_line={}
data_line['time']=time
data_line['heal']=heal
data_line['confirm']=confirm
data_line['dead']=dead

data_line=json.dumps(data_line)








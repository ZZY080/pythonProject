import requests
import json
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
url="https://c.m.163.com/ug/api/wuhan/app/data/list-total?t=1671770092303"
content=requests.get(url=url,headers=headers).text

content_dic=json.loads(content).get("data").get("areaTree")[2].get("children")[9].get("children")
print(content_dic)

total_data=[]
rename=["酉阳县","秀山县","彭水县","石柱县"]
for item in content_dic:
    data_dic={}
    name=item.get('name')
    value=item.get("total").get("confirm",0)
    if name in rename:
        if name in rename[:2]:
            data_dic["name"]=name[0:2]+'土家族苗族自治县'
        elif name in rename[2]:
            data_dic["name"] = name[0:2] + '苗族土家族自治县'
        elif name in rename[3]:
            data_dic["name"] = name[0:2] + '土家族自治县'
    else:
        data_dic["name"] = name
    data_dic["value"] = value
    total_data.append(data_dic)
# print(total_data)

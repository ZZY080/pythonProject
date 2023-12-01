import  requests
import  json
import pandas as pd
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

url="https://static.ws.126.net/163/f2e/news/virus_province/static/chongqing.json"

# 获取json数据
content=requests.get(url,headers=headers).text

# 利用json转成字典
content_dict=json.loads(content)

# 获取目标数据 即键为features的数据 数据类型为 列表内嵌入字典 38条数据
content_features=content_dict['features']

# 数据数量打印
print(len(content_features))

# 将每一个字段数据保存在列表中
type_list,id_list,cp_list,name_list,childNum_list=[],[],[],[],[]
# 对列表进行遍历 拿到每一个字典
for item_dict in content_features:
        type=item_dict["type"]
        id=item_dict["id"]
        cp=item_dict["properties"].get('cp',"暂无数据")
        name=item_dict["properties"].get("name","暂无数据")
        childNum=item_dict["properties"].get('childNum',"暂无数据")
        type_list.append(type)
        id_list.append(id)
        cp_list.append(cp)
        name_list.append(name)
        childNum_list.append(childNum)

# 转化为DataFrame格式 并将列表中的数据一次写入
dataframe=pd.DataFrame({"type":type_list,"id":id_list,"cp":cp_list,"name":name_list,"childNum":childNum_list})
dataframe.to_csv("province_2022_12_23.csv",index=False,header=True,encoding='gbk')




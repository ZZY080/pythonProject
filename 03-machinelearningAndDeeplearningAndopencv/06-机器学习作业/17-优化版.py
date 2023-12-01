import  requests
import  json
import time
import pandas as pd

# 获取数据 返回值为元组 元组内为各字段的数据 （type_list,id_list,cp_list,name_list,childNum_list）
def get_data(url):
    # 获取json数据
    content = requests.get(url).text
    # 利用json转成字典
    content_dict = json.loads(content)
    # 获取目标数据 即键为features的数据 数据类型为 列表内嵌入字典 38条数据
    content_features = content_dict['features']
    # 将每一个字段数据保存在列表中
    type_list, id_list, cp_list, name_list, childNum_list = [], [], [], [], []
    # 对列表进行遍历 拿到每一个字典
    for item_dict in content_features:
        type = item_dict["type"]
        id = item_dict["id"]
        cp = item_dict["properties"].get('cp', "暂无数据")
        name = item_dict["properties"].get("name", "暂无数据")
        childNum = item_dict["properties"].get('childNum', "暂无数据")
        type_list.append(type)
        id_list.append(id)
        cp_list.append(cp)
        name_list.append(name)
        childNum_list.append(childNum)
    return type_list,id_list,cp_list,name_list,childNum_list
def save_data(data,filename):
    # 解包
    (type_list,id_list,cp_list,name_list,childNum_list)=data
    # 转化为DataFrame格式 并将列表中的数据一次写入 每个列表代表一个字段的所有数据
    dataframe = pd.DataFrame({"type": type_list, "id": id_list, "cp": cp_list, "name": name_list, "childNum": childNum_list})
    dataframe.to_csv(f"{filename}.csv", index=False, header=True, encoding='utf8')

url = "https://static.ws.126.net/163/f2e/news/virus_province/static/chongqing.json"
# 获取数据
data=get_data(url)
filename=time.strftime('%Y-%m-%d',time.localtime(time.time()))
save_data(data,filename)
import pandas as pd
import  pymongo
# 得到数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 新建数据库
mydb=myclient["justeasy"]
# 创建集合
mycol = mydb["info"]
# 查询所有文档的 id 字段
mongo_all_id = mycol.find({}, {"_id": 0,"id": 1})
mongo_list_id = [doc["id"] for doc in mongo_all_id]
# 读取 Excel 文件 从200行开始
df = pd.read_excel('./全景1.xls',header=None)
part_id_list = df.iloc[:, 0].tolist()[:181]  # 选择第一列并转换为列表
part_id_list.extend(mongo_list_id)
part_id_list=list(set(part_id_list))



# # 读取 CSV 文件并取消索引
df = pd.read_csv('all.csv', index_col=False,header=None)

# 获取第一列数据并转换为列表 从第1500行开始
all_id_list = df.iloc[:, 0].tolist()[1301:]  # 获取第一列数据并转换为列表


id_list= [item for item in all_id_list if item not in part_id_list ]







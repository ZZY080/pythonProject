import  pymongo

# 得到数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 新建数据库
mydb=myclient["justeasy"]
# 创建集合
mycol = mydb["info"]
# 查询所有文档的 id 字段
all_id = mycol.find({}, {"_id": 0,"id": 1})

id_list = [doc["id"] for doc in all_id]
print(len(id_list))
print(id_list)
import  pymongo

# 得到数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 新建数据库
mydb=myclient["justeasy"]
# 创建集合
mycol = mydb["info"]

# 更新所有 iserror 为 true 的文档，将 isfinsh 设为 false
myquery = { "iserror": True }
newvalues = { "$set": { "isfinsh": False } }

result = mycol.update_many(myquery, newvalues)

print(result.modified_count, "文档已更新")
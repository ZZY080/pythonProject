import  pymongo

# 得到数据库连接
myclient = pymongo.MongoClient("mongodb://localhost:27017/")



# 新建数据库
mydb = myclient["demo"]
# 创建集合
mycol=mydb["user"]
# 插入一条文档
mydict = {"name":"kenny","age":12,"sex":"男"}
mycol.insert_one(mydict)
# 插入多条文档
mylist=[
{"name": "kenny", "age": 13, "sex": "男"},
{"name": "kenny", "age": 12, "sex": "男"},
]
mycol.insert_many(mylist)

# 查询一条文档
selectOne=mycol.find_one()
print(selectOne)

# 查询集合中所有文档
selectMany1 = mycol.find()
for item in selectMany1:
    print(item)

# 查询指定字段
selectMany2 = mycol.find({},{"_id":0,"name":1,"age":1});
for item in selectMany2:
    print(item)
print("------------------------------------")
# 查询符合条件的数据
selectSuit = mycol.find({"age":13})
for item in selectSuit:
    print(item)
print("------------------------------------")
# 比较查询 $gt $lt $gte  $lte
selectCompare = mycol.find({"age":{"$gt":12}})
for item in selectCompare:
    print(item)
print("------------------------------------")
# 返回指定条数的文档
selectLimt = mycol.find().limit(3)
for item in selectLimt:
    print(item)
print("------------------------------------")
# 修改一条文档
myQuery={'name':"kenny"}
newValues={"$set":{"name":"novia"}}
modifyOne=mycol.update_one(myQuery,newValues)
for item in mycol.find():
    print(item)
print("------------------------------------")
# 修改多条文档
modifyMany=mycol.update_many(myQuery,newValues)
for item in mycol.find():
    print(item)
print("------------------------------------")
# 文档排序
sorts=mycol.find().sort("id")
sorts=mycol.find().sort("id",-1)
for item in sorts:
    print(item)
print("------------------------------------")
# 删除一条文档
myQuery={"age":12}
mycol.delete_one(myQuery)
# 删除多条文档
mycol.delete_many(myQuery)
# 删除所有文档
myQuery={}
mycol.delete_many(myQuery)
# 删除集合
mycol.drop()

# 获取数据库名字
dblist = myclient.list_database_names()
print(dblist)





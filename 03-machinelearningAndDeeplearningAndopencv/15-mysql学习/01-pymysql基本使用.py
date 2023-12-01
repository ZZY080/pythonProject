import pymysql

# 建立数据库连接
mysqlClient = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="ZZY806@!.",
    database="pymysql",
    port=3306,
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

# 创建游标对象
cursor = mysqlClient.cursor()
# 创建sql语句 注意这里的sql语句要以;结尾
sql = "select * from user where id = %s or username = %s;"

# 执行sql语句
cursor.execute(sql,args=(1,"novia"))
mysqlClient.commit()

# 获取执行结果,单条数据
# result = cursor.fetchone()
result = cursor.fetchall()
print(result)

# 关闭连接 释放资源 先关闭游标 再关闭数据库连接对象
cursor.close()
mysqlClient.close()

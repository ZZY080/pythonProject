import pandas as pd

df1 = pd.read_json("./site.json")
# to_string() 用于返回 DataFrame 类型的数据，我们也可以直接处理 JSON 字符串。
print(df1.to_string())

# 接将 Python 字典转化为 DataFrame
# 字典格式的 JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame
df2 = pd.DataFrame(s)
print(df2)

# 从 URL 中读取 JSON 数据：
URL = 'https://static.runoob.com/download/sites.json'
df3=pd.read_json(URL)
print(df3.to_string())
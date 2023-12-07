import pandas as pd
from flask import  Flask
from flask_cors import CORS

app = Flask(__name__)
# 初始化 CORS 扩展
CORS(app)
@app.route("/getdata")
def getdata():
    # 读取 Excel 文件
    df1 = pd.read_excel('./全景1.xls')
    df1_col=df1.iloc[:, 0].tolist()[:180]  # 选择第一列并转换为列表
    print(df1_col)
    df2 = pd.read_csv("./全景2.xls")
    # 提取第一列数据（假设你需要的数据在第一列）
    column_values1 = df2.iloc[:, 0].tolist()  # 选择第一列并转换为列表
    column_values2= df2.iloc[:, 1].tolist()  # 选择第一列并转换为列表
    newdata=[];
    for i  in range(len(column_values1)):
        obj ={}
        obj["id"]=column_values1[i]
        obj["url"]=column_values2[i]
        newdata.append(obj)
    return newdata

if __name__=="__main__":
    app.run(debug=True,host="192.168.1.140",port=8081)


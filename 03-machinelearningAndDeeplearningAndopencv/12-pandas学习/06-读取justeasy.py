import pandas as pd

# 读取 Excel 文件 从200行开始
df = pd.read_excel('./全景1.xls',header=None)
part_id_list = df.iloc[:, 0].tolist()[:181]  # 选择第一列并转换为列表
# 读取 CSV 文件并取消索引
df = pd.read_csv('all.csv', index_col=False,header=None)

# 获取第一列数据并转换为列表 从第1500行开始
all_id_list = df.iloc[:, 0].tolist()[1301:]  # 获取第一列数据并转换为列表
id_list= [item for item in all_id_list if item not in part_id_list ]

# print(id_list.index(29415457))
# print(id_list)

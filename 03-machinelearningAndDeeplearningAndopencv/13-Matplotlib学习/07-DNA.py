import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 示例 DNA 序列
dna_sequence = "ATCGATCGATCGATCG"

# 计算每种碱基的数量
a_count = dna_sequence.count('A')
t_count = dna_sequence.count('T')
c_count = dna_sequence.count('C')
g_count = dna_sequence.count('G')

# 碱基名称和数量
bases = ['A', 'T', 'C', 'G']
counts = [a_count, t_count, c_count, g_count]

# 创建条形图
plt.bar(bases, counts, color=['blue', 'green', 'red', 'purple'])

# 添加标题和标签
plt.title('DNA 碱基组成')
plt.xlabel('碱基')
plt.ylabel('数量')

# 显示图表
plt.show()

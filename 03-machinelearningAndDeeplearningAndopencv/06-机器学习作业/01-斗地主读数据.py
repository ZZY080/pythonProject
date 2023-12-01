def train(filename):
    with open(filename,'r',encoding='utf8') as f:
        contentlist=f.readlines()
        if '\n' in contentlist:
            index=contentlist.index('\n')
            contentlist = contentlist[1:index]
        return len(contentlist)

file_path='./data/1.斗地主模拟结果1.txt'
length=train(file_path)
print(length)
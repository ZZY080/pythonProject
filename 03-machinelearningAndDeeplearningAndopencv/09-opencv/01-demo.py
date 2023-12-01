from paddlenlp import Taskflow
schema = ['名称', '毕业院校', '职位', '月收入', '身体状况']
ie = Taskflow('information_extraction', schema=schema)
print(ie("12343resdwerefdser"))
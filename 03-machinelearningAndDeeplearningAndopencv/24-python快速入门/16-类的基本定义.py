class People:
    '帮助信息'
    number = 100
    def __init__(self,name,age):
        self.name = name
        self.age=age

a=People("kenny",18)
# 判断对象 有没有 age 属性
print(hasattr(a,"age"))
print(setattr(a,"age",19))
print(getattr(a,"age"))
# print(delattr(a,"age"))
# print(getattr(a,"age"))

print(People.__doc__)
print(People.__name__)
print(People.__module__)
print(People.__bases__)
print(People.__dict__)


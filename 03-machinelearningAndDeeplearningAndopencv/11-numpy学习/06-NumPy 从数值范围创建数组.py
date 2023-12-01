import  numpy as np

a=np.arange(5)
print(a)

b=np.arange(5,dtype=float)
print(b)

c=np.arange(10,20,2,dtype=float)
print(c)

d=np.linspace(2,10,10)
print(d)

e=np.linspace(10,20,5,endpoint=False)
print(e)

f=np.linspace(1,10,10,retstep=True)
print(f)

g=np.linspace(1,10,10).reshape([10,1])
print(g)

# 创建等比数列 默认底数为10
h=np.logspace(1.0,2.0,num=10)
print(h)

i=np.logspace(0,9,10,base=2)
print(i)
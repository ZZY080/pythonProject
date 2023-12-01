import  numpy as np

a=[1,2,3]
b=np.asarray(a)
print(b)

c=(1,2,3)
d=np.asarray(c)
print(d)

e=[(1,2,3),(4,5,6)]
f=np.asarray(e)
print(f)

g=[1,2,3]
h=np.asarray(g,dtype=float)
print(h)

i=b"Hello World"
j=np.frombuffer(i,dtype="S1")
print(j)

k=range(5)
l=iter(k)
m=np.fromiter(l,dtype=float)
print(m)
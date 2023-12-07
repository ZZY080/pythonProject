import  torch
from torch.autograd import  Variable

N,D=(2,2)

x=Variable(torch.randn(N,D),requires_grad=True)
print("x:",x)
y=Variable(torch.randn(N,D),requires_grad=True)
print("y:",y)
z=Variable(torch.randn(N,D),requires_grad=True)

a=x*y
print("a:",a)
print("z:",z)
b=a+z
print("b:",b)
c=torch.sum(b)
print(c)
c.backward()
print(x.grad.data)
print(y.grad.data)
print(z.grad.data)

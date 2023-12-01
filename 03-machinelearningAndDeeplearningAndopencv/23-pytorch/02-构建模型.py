import torch
import  torch.nn as nn

# 定义模型
class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.fc1=nn.Linear(784,64)
        self.relu = nn.ReLU()
        self.fc2=nn.Linear(64,10)
        self.softmax = nn.Softmax(dim=1)

    def forward(self,x):
        x=self.fc1(x)
        x=self.relu(x)
        x=self.fc2(x)
        x=self.softmax()
        return x
# 创建模型实例
model = MyModel()

# 训练模型
# 准备训练数据和标签
train_data = ...
train_labels = ...

# 定义损失函数和优化器
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 训练模型
for epoch in range(10):
    optimizer.zero_grad()
    outputs = model(train_data)
    loss = criterion(outputs, train_labels)
    loss.backward()
    optimizer.step()
# 保存模型
torch.save(model.state_dict(), 'my_model.pth')
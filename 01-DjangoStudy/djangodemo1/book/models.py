from django.db import models

# Create your models here.

class BookInfo(models.Model):
    """
    主键 当前会自动帮助我们创建
    """
    name=models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    # 性别
    gender=models.BooleanField()
    # 外键
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

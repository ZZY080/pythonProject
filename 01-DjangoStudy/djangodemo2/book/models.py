from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name=models.CharField(max_length=10,unique=True,verbose_name='名字')
    pub_date=models.DateField(null=True)
    readcount=models.IntegerField(default=0)
    commentcount=models.IntegerField(default=0)
    is_delete=models.BooleanField(default=False)
    class Meta:
        # 改表名
        db_table='bookinfo'
        # 修改后台admin的显示信息的配置
        verbose_name_plural='书籍'
    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    GENDER_CHOICES=(
        (0,'MALE'),
        (1,'FEMALE'),
    )
    name=models.CharField(max_length=10,verbose_name='名称')
    gender=models.SmallIntegerField(choices=GENDER_CHOICES,default=0,verbose_name='性别')
    description=models.CharField(max_length=200,null=True,verbose_name='描述信息')
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete=models.BooleanField(default=False,verbose_name='逻辑删除')
    class Meta:
        db_table='peopleinfo'
        verbose_name_plural='人物信息'
    def __str__(self):
        return  self.name




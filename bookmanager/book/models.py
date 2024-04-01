from django.db import models

# Create your models here.
#1我们的模型类 需要继承自models.Model
#2系统会自动为我们添加一个主键 --id
#3字段
    #字段名=model.类型（选项）
    #字段名就是数据表的字段名
    #名字不要使用python，mysql等关键字
class BookInfo(models.Model):
    #id
    name = models.CharField(max_length=10)
#人物 先复制过来 后期讲原理
# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)


# -*- coding:utf-8 -*-
from django.db import models
# Create your models here.


# 作者
class  Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    #__str__() 方法告诉 Python 如何实现对象的字符串表示。 return self.first_name 表示显示对象的 first_name
    def __str__(self):
        return self.first_name

# 出版商
class  Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

# 书
class  Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)  #定义 books 与 author 是多对多的关系，一本书可以有多个作者，一个作者也可以写多本书。
    publisher = models.ForeignKey(Publisher)  #创建外键 在 book 类（表）中定义出版商的外键。
    publication_date = models.DateField()

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=20,verbose_name='图书名称')
    descript = models.TextField(verbose_name='书籍简介')
    publishdate = models.DateField(verbose_name='出版日期')
    #外键 多对一关系 加上on_delete属性
    #book中的publishing是外键 一本书只能有一个出版社 一个出版社可以有多个书
    publishing = models.ForeignKey(to='publishing',on_delete=models.CASCADE,verbose_name='出版社')
    #多对多 一本书可以有多个作者 一个作者可以写多本书
    author = models.ManyToManyField(to='author',verbose_name='作者')
    class Meta:
        verbose_name = '图书信息'
        verbose_name_plural = '图书信息'
    def __str__(self):
        return str(self.title) + '--相关图书信息'


class Publishing(models.Model):
    name = models.CharField(max_length=20,verbose_name='出版社名称')
    address = models.CharField(max_length=10,verbose_name='出版社地址')
    class Meta:
        verbose_name = '出版社信息'
        verbose_name_plural = '出版社图书信息'
    def __str__(self):
        return '社名: '+str(self.name)



class Author(models.Model):
    name = models.CharField(max_length=10,verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    birthday = models.DateField(verbose_name='出生日期')
    header = models.ImageField('作者头像')

    class Meta:
        verbose_name = '作者基本情况'
        verbose_name_plural = '作者基本情况'

    def __str__(self):
        return '作者：' + str(self.name)


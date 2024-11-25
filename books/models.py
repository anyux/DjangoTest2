from django.db import models

# Create your models here.

#定义图书模型类Book
class Book(models.Model):
    title = models.CharField(max_length=100,verbose_name="图书名称")
    read = models.IntegerField(default=0,verbose_name="阅读量")
    comment = models.IntegerField(default=0,verbose_name="评论量")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "图书"

#定义人物表
class Person(models.Model):
    name = models.CharField(max_length=20,verbose_name="人物名称")
    gender = models.BooleanField(default=True,verbose_name="性别")
    book = models.ForeignKey('Book',verbose_name="所属图书",on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = "person"
        verbose_name = "人物"

#人物与图书表的关系为一对多
from datetime import datetime

from django.db import models


# Create your models here.
class Books(models.Model):
    id = models.CharField(max_length=20, primary_key=True, verbose_name="图书编号",help_text="图书编号")
    name = models.CharField(max_length=50, verbose_name="书名",help_text="书名")
    status = models.BooleanField(default=False,verbose_name="是否出借,False表示未出借,True表示出借")

    class Meta:
        db_table = 'books'
        verbose_name = "图书表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Record(models.Model):
    book = models.ForeignKey('Books', on_delete=models.CASCADE, verbose_name="书籍")
    name = models.CharField(max_length=20, verbose_name="出借人")
    # 设置auto_created:数据创建时自动设置为当前时间
    # auto_now=True:当数据任何一个字段发生修改,都自动更新时间
    s_date = models.DateTimeField(verbose_name="出借时间", auto_now_add=True, auto_created=True)
    e_date = models.DateTimeField(verbose_name="归还时间", auto_now=True, auto_created=True)
    state = models.BooleanField(default=False, verbose_name="是否归还",db_comment="是否归还,False表示归,True表示出借")

    class Meta:
        db_table = 'record'
        verbose_name = "借还记录表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

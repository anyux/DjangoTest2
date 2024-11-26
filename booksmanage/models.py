from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.CharField(max_length=100, primary_key=True,verbose_name="图书编号")
    name=models.CharField(max_lenght=50,verbose_name="书名")
    status = models.CharField
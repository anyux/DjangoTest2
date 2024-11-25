from django.db import models

# Create your models here.

"""

#新闻类型表
     news_type表
        id:主键
        name:类型名称

#新闻信息表
     newsinfo表
         id:主键
         title:标题
         content: 内容
         read:阅读数量
         comment: 评论数据

数据表间关系:
     1对1: OneToOneField:1对1,将字段定义在任意一端中
     1对多: ForeignKey: 1对多,将字段定义在多的一端中
     多对多: ManyToManyField:多对多,将字段定义在任意一端中


"""


class NewsType(models.Model):
    '''
    定义新闻类型的模型类
    '''
    name = models.CharField(max_length=20, null=True, blank=True, verbose_name="新闻分类", help_text="名称")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    # __str__方法的作用,可以更改对象显示的内容
    # print打印对象时,默认显示str方法的内容
    #
    def __str__(self):
        return self.name

    class Meta:
        # 默认生成的表名时,应用名_模型类名小写
        # 对过db_table指定表名称
        db_table = 'type'
        # 表的说明信息,在django后台可以看到
        verbose_name = '新闻类型'


class NewsInfo(models.Model):
    """
    新闻信息的模型类
    """
    title = models.CharField(max_length=100, verbose_name="标题", help_text="内容")
    content = models.TextField(verbose_name="内容", help_text="内容")
    read = models.IntegerField(verbose_name="阅读量", help_text="阅读量")
    comment = models.IntegerField(verbose_name="评论数量", help_text="评论数量")
    # 维护多对多的关联关系
    type = models.ManyToManyField(NewsType, verbose_name="新闻类型", help_text="新闻类型")
    created = models.DateTimeField(auto_now_add=True, verbose_name="创建时间", help_text="创建时间")
    updated = models.DateTimeField(auto_now=True, verbose_name="更新时间", help_text="更新时间")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'news'
        verbose_name = "新闻表"

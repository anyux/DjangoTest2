from django.contrib import admin

# 导入模型类
from news.models import NewsInfo,NewsType

# Register your models here.

class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title','content','read']


#注册到admin后台
admin.site.register(NewsType,NewsTypeAdmin)
admin.site.register(NewsInfo,NewsInfoAdmin)

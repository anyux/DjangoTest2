from django.contrib import admin

# 导入模型类
from books.models import Book,Person

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title','read','comment']

class PersonAdmin(admin.ModelAdmin):
    list_display = ['id','name','gender','book']


#注册到admin后台
admin.site.register(Book,BookAdmin)
admin.site.register(Person,PersonAdmin)

# Register your models here.

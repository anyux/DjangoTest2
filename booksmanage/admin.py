from django.contrib import admin

from booksmanage.models import Books, Record


# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 's_date', 'e_date', 'state', 'book']


# 注册到admin后台
admin.site.register(Books, BooksAdmin)
admin.site.register(Record, RecordAdmin)

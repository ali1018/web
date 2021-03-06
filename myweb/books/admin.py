# -*- coding:utf-8 -*-
from django.contrib import admin
from books.models import *
# Register your models here.

class  AutAdmin(admin.ModelAdmin):  #继承admin.ModelAdmin
    list_display = ('first_name', 'last_name', 'email')  #列表返回

class  PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state_province', 'country', 'website')

class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')

admin.site.register(Author, AutAdmin)  #admin.site.register()将 Author 与 AutAdmin 对应。
admin.site.register(Publisher, PubAdmin)
admin.site.register(Book, BookAdmin)
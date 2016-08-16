# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
# Create your views here.
# sutdent list
from books.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#实现分页的类

def  table(request):
    books = Book.objects.all()
    paginator = Paginator(books, 2) # 分页展示
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('table.html',  {'book_list': books,'pages': contacts})



# file upload page
def  upload(request):
    return render_to_response('upload.html')
    # file upload save

def  upload_save(request):
    files = File.objects.all()
    filename = request.POST.get('filename', '') # 获得表单文件说明
    fileing = request.FILES.get('fileing', '') # 获得文件
    if filename == '' or fileing == '':
        error = 'File and description cannot be empty!'
        return render_to_response('upload.html', {'error': error, 'file_list': files})
    else:
        upload = File()
        upload.filename = filename
        upload.fileway = fileing
        upload.save()
        return render_to_response('upload.html', {'upload_success': 'uploadsuccess!','file_list': files})
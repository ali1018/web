from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from blog.models import Blog
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

#from myweb.blog.models import Blog

user = [0]
username = [0]

@login_required
def index(request):
    blog_list = Blog.objects.all()  #定义blog的列表 继承 Blog的属性
    #username = request.COOKIES.get('username', '')  # 读取浏览器 cookie
    username = request.session.get('username','') #读取用户session
    user = username[0]
    return render_to_response('index.html', {'user': user,'blogs': blog_list})  #返回blog的内容到index

def login(request):
    return render(request,'login.html')

def login_action(request):
    username = request.GET.get('username', '') #获取数据
    password = request.GET.get('password', '')
    users_ = [username]
    # authenticate()函数。 它接受两个参数， 用户名 username 和密码 password，并在密码对给出的用户名合法的情况下返回一个 user 对象。 如果密码不合法，authenticate()返回 None。
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)  #验证登录
        response = HttpResponseRedirect('/index/')
        request.session['username'] = users_
        return  response
    else:
        return render_to_response('login.html', {'error': 'username or passworderror!'})

@login_required
def  logout(request):
    response = HttpResponseRedirect('/login/') # 返回登录页面
    #response.delete_cookie('username') # 清理 cookie 里保存 username
    del request.session['username']  #清理用户session
    return response


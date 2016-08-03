from django.template import RequestContext
from django.contrib import auth
from .models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# login blog
@login_required
def index(request):
    blog_list = Blog.objects.all()
    # username = request.COOKIES.get('username', '') # 读取浏览器 cookie
    username = request.session.get('username', '') # 读取用户 session
    user = username[0]
    return render_to_response('index.html',
    {'user': user, 'blogs': blog_list})



# user login
def login(request):
    return render(request, 'login.html')

# validate logon
def login_action(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    users_ = [username]
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user) # 验证登录
        response = HttpResponseRedirect('/index/')
        request.session['username'] = users_
        return response
    else:
        return render_to_response('login.html',
        {'error': 'username or password error!'},
        context_instance=RequestContext(request))

# logout
@login_required
def logout(request):
    response = HttpResponseRedirect('/login/') # 返回登录页面
    # response.delete_cookie('username') # 清理 cookie 里保存 username
    del request.session['username'] # 清理用户 session
    return response
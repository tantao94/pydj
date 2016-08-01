from .models import Blog
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    blog_list = Blog.objects.all()
    return render_to_response('index.html',{'blogs':blog_list})

# def login(request):
#     username=request.POST.get('username','')
#     password=request.POST.get('password','')
#     if username == 'sunlin' and password == '123456':
#         return HttpResponse('login success')
#     else:
#         return render_to_response('index.html',{'error':'username and password error'})
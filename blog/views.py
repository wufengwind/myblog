# Create your views here.
from blog.models import Essay, User
from django.shortcuts import render, HttpResponse, HttpResponseRedirect,redirect
import datetime
import json

def index(request):
    return render(request, "index.html")

def viwe(request):
    return render(request, "essay.html")
def have_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False
def essay(request):
    import random
    if request.method == 'GET':
        kinds=request.GET.get('kind')
        articles=Essay.objects.filter(kind=kinds)
        count=articles.count()
        try:
            num=random.randint(0,count-4)
            data=articles[num:num+4]
            return render(request, 'index.html', {'data': data})
        except:
            return HttpResponse("这个板块目前空空如也")

def write(request):
    return render(request, "write.html")

def viewone(request):
    if request.method=='GET':
        try:
            title=request.GET.get('title')
            username=request.GET.get('thename')
            articles = Essay.objects.filter(username=username,title=title)
            data=articles[0]
            # data.time=data.time[0:-5]
            return render(request, 'essay.html', {'data': data})
        except:
            return HttpResponse('由于数据源错误，这篇文章无法显示')
    else:
        return HttpResponse('出现未知错误')

def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('re_name')
        pwd = request.POST.get('re_pass')
        User.objects.create(username=name, photo=pwd)
        return HttpResponseRedirect('/login/')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        # name=name.encode('ISO-8859-1').decode('utf-8')
        pwd = request.POST.get('pass')
        user_obj = User.objects.filter(username=name, photo=pwd).first()
        if user_obj:
            name=json.dumps(name)
            response = HttpResponseRedirect('/index/')
            response.set_cookie('username', name, max_age=360000)
            return response
    else:
            return HttpResponse('用户名或密码错误')

def logout(request):
    pass

def pulish(request):
    if request.method=='POST':
        kind=request.POST.get('select')
        content=request.POST.get('description')
        time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        title=request.POST.get('title')
        try:
            username=request.COOKIES['username']
            username = json.loads(username)
        except:
            return HttpResponse("请先登录")
        else:
            user_obj = Essay.objects.create(kind=kind, essay=content,time=time,username=username,title=title)
            if user_obj:
                # msg='发表成功'
                # return render(request, 'write.html')
                return HttpResponse('发表成功')
            else:
                # msg='提交失败'
                return HttpResponse('发表失败')

def search(request):
    from django.db.models import Q
    if request.method=='GET':
        title=request.GET.get('sousou')
        Articles=Essay.objects.filter(Q(title__contains=title)|Q(username__contains=title)|Q(essay__contains=title))

        if Articles.count()>0:
            datax = Articles
            return render(request, 'index.html', {'data': datax})
        else:
            return HttpResponse('抱歉，没有这篇或没有与这篇类似的文章')

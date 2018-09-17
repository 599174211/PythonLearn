from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request) :
    #增加数据
    # s1 = Student(name='xiaowang', age =18)
    # s1.save()
    #删除 pk代表主键
    # Student.objects.filter(name = 'xiaowang').delete()
    #修改
    # s = Student.objects.get(id = 8)
    # s.name = 'liuge'
    # s.save()
    #查询多条
    # s = Student.objects.filter()
    #查询单条
    #exact表示等于iexact使用的like
    # s = Student.objects.filter(pk__exact=8)
    # s = Student.objects.filter(name__iexact = 'xiaowang')
    #     # print(s.query)
    #     # for i in s :
    #     #     print(i)
    #contains包含字符串区分大小写icontains不区分大小写
    s = Student.objects.filter(name__contains= 'Xiao')
    # s = Student.objects.filter(name__icontains= 'Xiao')
    print(s.query)
    for i in s :
        print(i)
    return HttpResponse('success query:')
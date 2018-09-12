from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.urls import reverse


def index(request) :
    name = request.GET.get('name')
    if name :
        request_methon = request.method;
        request_encoding = request.encoding;
        request_cookies = request.COOKIES
        request_host = request.get_host()
        return HttpResponse('Hello Python! {},methon:{},encodind:{},cookeies{}, host{}'.format(name,request_methon, request_encoding
                                                            ,request_cookies, request_host))
    else:
        return HttpResponse('没有传入参数!')
def index2(requst, number) :
    return HttpResponse('Hello Python!{}'.format(str(number)))
def index3(request) :
    return HttpResponse(reverse('python2:index'))
def page(requset, pg) :
    return HttpResponse('Hello Python!{}'.format(str(pg)))
def exception(request) :
    raise Http404
    return HttpResponse('exception')
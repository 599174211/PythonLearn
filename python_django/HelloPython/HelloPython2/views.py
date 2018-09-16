from django.shortcuts import render,render_to_response,reverse
from django.http import HttpResponse,Http404,HttpResponseNotFound
from django.template import loader
from django.views import defaults
from datetime import datetime

def index(request) :
    dict_index = {
        'name' : ['python', 'java'],
        'datetime': datetime.now()
    }
    re = render(request, 'index.html', dict_index)
    return re
def index1(request) :
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
def request_item(request) :
    request_dict = {}
    for k, v in request.GET.items() :
        request_dict[k] = v
    return HttpResponse(str(request_dict))
def for_post(request) :
    return render_to_response('forpost.html')
def forrender(request) :
    c = dict();
    c['name'] = str(reverse('python2:forrender'))
    c['age'] = 18
    re = render(request,'render.html', context = c)
    return re;
def forrender1(reques) :
    #得到一个模块
    t = loader.get_template('render.html')
    re = t.render({'name' : 'python', 'age' : 20})
    return HttpResponse(re)
def forrender2(request) :
    re = render_to_response('render.html', context={'name' : 'python', 'age' : 21})
    return HttpResponse(re)

def for404(request) :
    return defaults.page_not_found(request, Exception.args, template_name='http404.html')

def extends_1(request) :
    return render(request, 'extends_1.html')
def base(request) :
    dic_url = {'company': reverse('python2:company')
               ,'school': reverse('python2:school')}
    return render(request, 'base.html',context= dic_url)
def company(request) :
    condext = {'name': 'hello'}
    return render(request, 'company.html',context= condext)
def school(request) :
    return render(request, 'school.html')
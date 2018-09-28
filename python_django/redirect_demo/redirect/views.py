from django.shortcuts import render,render_to_response,reverse
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_GET,require_http_methods,require_POST
from django.http.request import HttpRequest,QueryDict
from django.core.cache import cache
from django.db.models import Avg,F,Q,Count,Sum
import json
# Create your views here.
@require_GET
def index(request,page):
    #index对应的path不包含请求的参数
    index_path = request.path
    print('index_path:{}'.format(index_path))
    #index获取完成的path包含请求的参数
    print(request.get_full_path)
    for key, value in request.META.items():
        print('key:{},value:{}'.format(key, value))

    person=[{
        'name':'xiaowang',
        'age': 18,
        'height': 18
        }]
    # person_json = json.dumps(person)
    # reponse = HttpResponse(person, content_type = 'application/json')
    json = JsonResponse(person, safe=False)
    return HttpResponse(json)
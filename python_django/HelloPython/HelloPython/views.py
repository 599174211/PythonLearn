from django.http import HttpResponse
from django.shortcuts import render_to_response,render,reverse

def post_for(request) :
    post_dict = dict({})
    str_post = ''
    #获取多个checkbox的值
    request_box = request.POST.getlist('uhobby')
    for k, v in request.POST.items() :
        post_dict[k] = v
        # str_post += k + '->' + v
    return HttpResponse(str(post_dict))
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
# Create your views here.
def index(request) :
    # art= Article(atc_name='清华出版社')
    # art.save()
    # tag = Tag(name='后楼梦')
    # tag.save()

    # tag.article.add(art)
    # art =Article.objects.first()
    # tag = Tag(name='水浒传')
    # tag.save()
    # art.tags.add(tag)

    # art = Article.objects.first()
    # tag = Tag.objects.first()
    # tag.article.add(art)

    # art = Article.objects.get(pk=1)
    # print('art{}'.format(art))
    # tag = art.tags.all()
    # for t in tag :
    #     print(t)
    tag = Tag.objects.get(pk = 1)
    print(connection.queries)
    article = tag.article.all()
    print(article.query)
    for art in article:
        print(art)
    return HttpResponse('success')
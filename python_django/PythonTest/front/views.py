from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db.models import Avg,Count
from django.db import connection
# Create your views here.
def index(request) :
    # result = Book.objects.aggregate(price_avg = Avg('price'))
    books = Book.objects.annotate(avg = Count('bookorder__book'))
    print(connection.queries)
    for book in books :
        print('{},{}'.format(book.name, book.avg))
    return HttpResponse('This is front index!')
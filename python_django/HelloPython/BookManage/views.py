from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.conf import settings
import pymysql
from BookManage.models import ManageBook
# Create your views here.
def getconect() :
    db = pymysql.connect(host = 'localhost',user = 'root', password= 'password', db = 'demo1', port = 3306)
    return db
def bookeIndex(request) :
    # try :
    #     db =getconect()
    #     print(db)
    #     cur = db.cursor()
    #     sql = 'select book_id,book_name,book_author from bookmanage_managebook'
    #     cur.execute(sql)
    #     result = cur.fetchall()
    #     return render(request,'book\index.html',context= {'books': result})
    # finally:
    #     db.close()
    books = ManageBook.objects.all();
    context_dict = dict()
    book_list = list()
    for book in books:
        book_l = list()
        book_l.append(book.book_id)
        book_l.append(book.book_name)
        book_l.append(book.book_author)
        book_list.append(book_l)
    print(book_list)
    context_dict['books'] = book_list
    print(context_dict)
    return render(request, 'book\index.html',context=context_dict)
def bookAdd(request) :
    if request.method == 'GET':
        return render(request,'book\inset_book.html')
    else :
        book_name=  request.POST.get('book_name')
        book_author=  request.POST.get('book_author')
        # db = getconect()
        # cur =db.cursor()
        # sql = 'insert into bookmanage_managebook(book_name, book_author) values ("%s","%s") ' %(book_name,book_author)
        # print('sql:{}'.format(sql))
        # cur.execute(sql)
        # db.commit()
        # db.close()
        book = ManageBook(book_name=book_name, book_author = book_author)
        book.save()
        return redirect(reverse('book:index'))

#书本详情
def bookContent(request, book_id):
    db = getconect()
    cur = db.cursor()
    sql = 'select book_id, book_name,book_author from  bookmanage_managebook where book_id = %s' %(book_id)
    print('sql:{}'.format(sql))
    cur.execute(sql)
    resutl = cur.fetchone()
    print('result:{}'.format(resutl))
    return render(request, 'book\content_book.html', {'book': resutl})

def bookDelete(request) :
    if request.method == 'POST':
        # db = getconect()
        bookid = request.POST.get('book_id')
        # cur = db.cursor()
        # sql = 'delete from bookmanage_managebook where book_id = %s' %(bookid)
        # cur.execute(sql)
        # db.commit()
        m = ManageBook.objects.get(book_id = bookid)
        print('type{}'.format(type(m)))
        m.delete()
        return redirect(reverse('book:index'))
    else:
        raise Exception('删除图书')

def bookUpdate(request) :
    if request.method == 'POST':
        bookid = request.POST.get('book_id')
        bookname = request.POST.get('book_name')
        bookauthor = request.POST.get('book_authon')
        print('id:{},name:{},autho:{}'.format(bookid,bookname,bookauthor))
        if bookname != '' and bookauthor != '':
            m = ManageBook.objects.get(book_id = bookid)
            m.book_name = bookname
            m.book_author = bookauthor
            m.save()
            return redirect(reverse('book:index'))
        else:
            raise Exception('异常操作')
    else:
        raise Exception('异常操作')
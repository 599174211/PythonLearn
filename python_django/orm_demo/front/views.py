from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Score, Teacher, Course
from django.db.models import Avg,Count,Sum,Q,F,Max, Min
from django.db import connection
# Create your views here.

def index(request) :
    #查找平均成绩大于60分的同学的id和平均成绩
    students = Student.objects.annotate(score_avg=Avg('score__number')).filter(score_avg__gt=60).values('id','score_avg')
    for student in students :
        print('student:{}'.format(student))
    return HttpResponse('success')
def index1(request):
    #查询所有同学的id，姓名，选课的数量和总成绩
    students = Student.objects.annotate(course_numbs = Count('score__id'),
                                        total = Sum('score__number')).values(
        'id', 'name', 'course_numbs', 'total'
    )
    for student in students :
        print('studet:{}'.format(student))
    return HttpResponse('success')
def index2 (request) :
    #查询姓李老师的个数
    teacher_num = Teacher.objects.filter(name__startswith='李').count()
    print('teacher_num:{}'.format(teacher_num))
    return HttpResponse('success')
def index3(request) :
    #查询所有学过李老师课的学生
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id', 'name')
    for student in students:
        print('student:{}',student)
    return HttpResponse('success')
def index4(request):
    #查询学过课程id为1和2的所有同学的id、姓名
    students = Student.objects.filter(score__course_id__in=[1,2]).values('id','name').distinct()
    for student in students:
        print('student{}'.format(student))
    return HttpResponse('success')

def index5(request):
    #查询过‘黄老师’所教的“所有课”的学生id、name
    #第一步首先找到每一位学生学习黄老师课程的数量     A
    #第二步在课程表中找到黄老师课程的数量 B
    #第三步判断A等于B 如果相等表示学生学习了黄老师的所有课程
    #如果不相等，意味着这个学生没有学习黄老师的所有课程
    students = Student.objects.annotate(nums = Count('score__course_id', filter= Q(score__course__teacher__name='黄老师')))\
        .filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id','name')
    for student in students:
        print('student:{}'.format(student))
    return HttpResponse('succes')
def index6(request):
    #7. 查询所有课程成绩小于60分的同学的id和姓名；
    students = Student.objects.exclude(score__number__gt=60).values('id','name')
    for student in students:
        print('student:{}'.format(student))
    return HttpResponse('success')
def index7(request):
    #查询没有学全所有课的同学的id、姓名；
    students=Student.objects.annotate(coure_len=Count('score__course')).\
        filter(coure_len=Course.objects.count()).values('id','name')
    # students = Student.objects.annotate(num=Count(F("score__course"))).\
    #     filter(num__lt=Course.objects.count()).values('id','name')
    for studen in students:
        print('student:{}'.format(studen))
    print(connection.queries)
    return HttpResponse('success')
def index8(request):
    #查询所有学生的姓名、平均分，并且按照平均分从高到低排序
    students = Student.objects.annotate(score_avg = Avg('score__number')).\
        order_by('score_avg').values('id','name','score_avg')
    for student in students:
        print('student:{}'.format(student))
    print(connection.queries)
    return HttpResponse('success')
def index9(request):
    #查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分：
    course = Course.objects.annotate(score_max = Max('score__number'),
                                     score_min = Min('score__number'),
                                     score_avg = Avg('score__number')).\
        values('id','name', 'score_max', 'score_min', 'score_avg')
    for cour in course:
        print('course:{}'.format(cour))
    print(connection.queries)
    return HttpResponse('success')

def index10(request):
    #查询每门课程的平均成绩，按照平均成绩进行排序
    course = Course.objects.annotate(score_avg = Avg('score__number')).order_by('score_avg')
    for cour in course:
        print('course:{},{}'.format(cour.name, cour.score_avg))
    print(connection.queries)
    return HttpResponse('success')

def index11(request):
    #统计总共有多少女生，多少男生
    rows = Student.objects.aggregate(boy_count = Count('gender',filter=Q(gender = 1)),
                                        gril_count = Count('gender',filter=Q(gender = 2)))
    print('rows:{}'.format(rows))
    print(connection.queries)
    return HttpResponse('success')

def index12(request):
    #将“黄老师”的每一门课程都在原来的基础之上加5分；
    rows = Score.objects.filter(course__teacher__name='黄老师').update(number=F('number') + 5)
    print('rows:{}'.format(rows))
    print(connection.queries)
    return HttpResponse('success')
def index13(request):
    #查询两门以上不及格的同学的id、姓名、以及不及格课程数
    studens =Student.objects.annotate(course_count = Count('score__number',
                                                          filter=Q(score__number__lt=60))).\
        filter(course_count__gte=2).values('id', 'name', 'course_count')
    for student in studens:
        print('student:{}'.format(student))
    print(connection.queries)
    return HttpResponse('success')
def index14(request):
    #查询每门课的选课人数；
    course = Course.objects.annotate(course_count = Count('score__student')).values('id','name','course_count')
    for cour in course:
        print('cour:{}'.format(cour))
    print(connection.queries)
    return HttpResponse('success')
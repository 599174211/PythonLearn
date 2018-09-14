from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import  datetime
class Teacher(models.Model) :
    name = models.CharField(max_length=12)
    age = models.IntegerField(max_length=3, null=True, default= 0)
    addres = models.CharField(max_length=50,default='changsha',null=True)
    course = models.CharField(max_length=200,default='wo like python',null=True)
    sex = models.IntegerField(max_length=1, default=0, null=True)

    def __str__(self):
        return self.name

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    def __str__(self):
        return self.school_name
class Manager(models.Model) :
    manager_id = models.IntegerField()
    manager_name = models.CharField(max_length=10)
    my_school = models.OneToOneField(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.manager_name

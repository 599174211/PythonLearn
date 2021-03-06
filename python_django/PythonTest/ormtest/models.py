from django.db import models

# Create your models here.
class Student(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return '<id:{},name:{},age:{}>'.format(self.id, self.name, self.age)
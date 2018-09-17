from django.db import models

# Create your models here.
class Tag(models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self):
        return '<name:{}>'.format(self.name)

class Article(models.Model) :
    atc_name = models.CharField(max_length=100)
    tags = models.ManyToManyField('Tag', related_name='article')

    def __str__(self):
        return '<atc_name:{}>'.format(self.atc_name)
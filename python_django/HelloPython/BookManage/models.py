from django.db import models

# Create your models here.
class ManageBook(models.Model) :
    book_id = models.AutoField(max_length=20,primary_key=True)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=50)

    def __str__(self):
        return self.book_name
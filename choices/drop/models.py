from django.db import models


CITY_CHOICES=(
    ('Delhi','Delhi'),
    ('Mumbai','Mumbai'),
    ('Bangluru','Bangluru'),
)

class book(models.Model):
    bookname=models.CharField(max_length=20)
    author=models.CharField(max_length=20)

    city=models.CharField(max_length=30,choices=CITY_CHOICES,default='Delhi')

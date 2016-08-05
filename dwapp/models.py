from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    cell_number = models.IntegerField(max_length=10)
    ticket_number =  models.CharField(max_length=20)
    structure =models.CharField(max_length=50)
    created_date= models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def sold(self):
        self.created_date=timezone.now()
        self.save()







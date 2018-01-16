from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class Student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=30)


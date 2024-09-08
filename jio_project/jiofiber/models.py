from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=8, decimal_places=2)
class Staff(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    experience = models.IntegerField()
    dept = models.CharField(max_length=100)
class Parents(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)

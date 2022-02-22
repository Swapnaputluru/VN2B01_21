from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=40)
    id = models.IntegerField(primary_key=True)


class Adddetails(models.Model):
    location = models.CharField(max_length=20)
    state= models.CharField(max_length=6)


class Demo(models.Model):
    name=models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    higher_education = models.CharField(max_length=20)
    passedout_year= models.IntegerField()

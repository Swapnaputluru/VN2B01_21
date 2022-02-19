from django.db import models

# Create your models here.
class Googlepay_details(models.Model):
    mobile_no=models.IntegerField()
    otp=models.IntegerField()

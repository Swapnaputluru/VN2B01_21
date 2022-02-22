from django.db import models

# Create your models here.


class Mark(models.Model):
    Student_name=models.CharField(max_length=40)
    Student_id = models.IntegerField(primary_key=True)
    Telugu_marks = models.IntegerField()
    English_marks = models.IntegerField()
    kannada_marks = models.IntegerField()
    Hindi_marks = models.IntegerField()
    Maths_marks = models.IntegerField()
    Science_marks = models.IntegerField()

    def __str__(self):
        return self.Student_name


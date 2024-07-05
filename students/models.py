from django.db import models

# Create your models here.

gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class Student(models.Model):
    roll_no = models.IntegerField()
    photo = models.ImageField(upload_to= 'photos/%y/%m/%d/')
    full_name = models.CharField(max_length=1000)
    course = models.CharField(max_length=1000)
    grade = models.CharField(max_length=1000)
    gender = models.CharField(choices=gender_choices, max_length=1000)

    def __str__(self):
        return self.full_name


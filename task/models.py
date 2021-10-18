from django.db import models
from django.core.validators import BaseValidator,MaxValueValidator,MinValueValidator


"""from phonenumber_field.modelfields import PhoneNumberField"""
# Create your models here.


class student(models.Model):

    student_name=models.CharField(max_length=200)
    fathers_name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True,verbose_name='DOB')
    Address=models.CharField(null=True,max_length=200)
    city=models.CharField(null=True,max_length=50)
    state=models.CharField(null=True,max_length=20)
    pin=models.IntegerField(max_length=7,null=True)
    phone=models.IntegerField(unique=True,max_length=10)
    email=models.EmailField(unique=True,null=True)
    class_opted=models.IntegerField(max_length=2,validators=[MinValueValidator(5),MaxValueValidator(10)])
    marks=models.IntegerField(verbose_name='Marks%',max_length=3,null=True)
    date_enrolled=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.student_name

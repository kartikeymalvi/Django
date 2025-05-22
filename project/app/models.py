from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=20, unique=True)
    
    detail = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    dob = models.DateField()
    subscribe = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='image/')
    resume = models.FileField(upload_to='file/')
    password = models.CharField(max_length=55)
    cpassword = models.CharField(max_length=50)

class Travel(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    dob=models.DateField()


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
    destination = models.CharField(max_length=100,null=True)
    duration = models.CharField(max_length=50,null=True)
    price = models.IntegerField()
    description = models.CharField(null=True)
    itinerary = models.CharField(null=True)
    image = models.ImageField(upload_to='image/')
    inclusions = models.CharField(null=True)
    exclusions = models.CharField(null=True)
    available_from = models.DateField()
    available_to = models.DateField()

    def __str__(self):
        return self.destination

class Booking(models.Model):
    place = models.ForeignKey(Travel, on_delete=models.CASCADE,)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
   

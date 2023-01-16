from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=300)
    age=models.IntegerField()
    email=models.EmailField()
    password=models.IntegerField()
class roomies(models.Model):
    roomname=models.CharField(max_length=250)
    roomno=models.IntegerField()
    description=models.CharField(max_length=300)
    image=models.ImageField(upload_to="pics")
class facility(models.Model):
    name = models.CharField(max_length=250)
    bookno = models.IntegerField()
    email = models.EmailField()


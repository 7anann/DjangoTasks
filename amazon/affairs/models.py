from django.db import models

# Create your models here.
class myuser(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    test=models.CharField(max_length=20)

class students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    track=models.CharField(max_length=20)

class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    fullname =models.CharField(max_length=20)
    sdate =models.DateField()
    edate =models.DateField()


class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

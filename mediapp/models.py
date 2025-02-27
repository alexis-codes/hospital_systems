from django.db import models

# Create your models here.

class patient(models.Model) :
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=150)
    date = models.DateField()
    message = models.TextField()


    def __str__(self):
        return self.name

class doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20)


    def __str__(self):
        return self.name

class staff(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    shift = models.CharField(max_length=10)


    def __str__(self):
        return self.name

class ward(models.Model):
    name = models.CharField(max_length=50)
    wing = models.CharField(max_length=15)
    beds = models.CharField(max_length=15)
    status = models.CharField(max_length=15)


    def __str__(self):
        return self.name

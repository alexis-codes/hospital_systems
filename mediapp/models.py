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

class Appointment1(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    department = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    message=models.TextField()

    def __str__(self):
        return self.name


class contact2(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name




#Mpesa API
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"


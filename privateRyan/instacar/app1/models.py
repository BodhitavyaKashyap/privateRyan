from django.db import models

# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    chargeperkm = models.IntegerField()
    profileurl  = models.CharField(max_length = 100)

class User(models.Model):
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    emailid = models.CharField(max_length = 254)
    password = models.CharField(max_length = 50)
    chargeperkm = models.IntegerField()
    profileurl  = models.CharField(max_length = 100)

class Order(models.Model):
    orderticket = models.IntegerField()
    customerid = models.ForeignKey(User,on_delete=models.CASCADE)
    destination= models.CharField(max_length = 50)
    price = models.IntegerField()
    driver =  models.ForeignKey(Driver,on_delete=models.CASCADE)

class Destination(models.Model):
    city = models.CharField(max_length = 50)
    distance =  models.IntegerField()

class Car(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500)
    pics  = models.CharField(max_length = 100)



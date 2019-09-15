from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers


#immport models
from app1 import models as app1models

order=app1models.Order()


# Create your views here.
def landingFunction(Request):
    return render(Request,'dashboard.html')

def getDestinations(Request):
    alldestinations = app1models.Destination.objects.all()
    return HttpResponse(alldestinations.values())

def getCars(Request):
    destination_id=Request.POST['destination']
    order.destination=destination_id
    allcars = app1models.Car.objects.all()
    return HttpResponse(allcars.values())

def getCarDetils(Request):
    getCarDetils = app1models.Car.objects.all()
    post_list = serializers.serialize('json', getCarDetils)
    return HttpResponse(post_list,content_type="text/json-comment-filtered")

def getDrivers(Request):
    car_id=Request.POST['car']
    order.car=car_id
    alldriver = app1models.Driver.objects.all()
    return HttpResponse(alldriver.values())

def getPrice(Request):
    driver_id=Request.POST['driver']
    order.driver=driver_id
    order.price=500
    return HttpResponse(order)

def saveOrder(Request):
    order.save()
    return HttpResponse(order)
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
    getDestin=app1models.Destination.objects.all()
    alldestinations = serializers.serialize('json',getDestin)
    return HttpResponse(alldestinations,content_type="text/json-comment-filtered")

def getCars(Request):
    print(Request.POST)
    destination_id=Request.POST['destination']
    start_date=Request.POST['start_date']
    end_date=Request.POST['end_date']
    trip_type=Request.POST['trip_type']
    print(destination_id,start_date,end_date,trip_type)
    order.destination=destination_id
    order.startdate=start_date
    order.end_date=end_date
    order.triptype=trip_type
    allcars = serializers.serialize('json',app1models.Car.objects.all())
    return HttpResponse(allcars,content_type="text/json-comment-filtered")

def getCarDetils(Request):
    getCarDetils = app1models.Car.objects.all()
    post_list = serializers.serialize('json', getCarDetils)
    return HttpResponse(post_list,content_type="text/json-comment-filtered")

def getDrivers(Request):
    car_id=Request.POST['car']
    order.car=car_id
    alldriver = serializers.serialize('json',app1models.Driver.objects.all())
    return HttpResponse(alldriver,content_type="text/json-comment-filtered")

def getPrice(Request):
    driver_id=Request.POST['driver']
    order.driver=driver_id
    order.price=500
    return HttpResponse(order)

def saveOrder(Request):
    order.save()
    return HttpResponse(order)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingFunction,name='landingFunction'),
    path('destinations',views.getDestinations),
    path('cars',views.getCars),
    path('drivers',views.getDrivers),
    path('price',views.getPrice)
]
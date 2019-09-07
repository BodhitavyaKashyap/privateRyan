from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingFunction,name='landingFunction'),
]
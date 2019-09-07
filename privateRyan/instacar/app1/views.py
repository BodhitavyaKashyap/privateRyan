from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingFunction(Request):
    return render(Request,'dashboard.html')
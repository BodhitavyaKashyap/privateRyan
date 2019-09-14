from django.contrib import admin
from app1 import models as app1models
# Register your models here.
admin.site.register(app1models.Driver)
admin.site.register(app1models.User)
admin.site.register(app1models.Order)
admin.site.register(app1models.Destination)
admin.site.register(app1models.Car)

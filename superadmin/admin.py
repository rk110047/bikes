from django.contrib import admin
from .models import State,City,BikeCompany,BikeModel

# Register your models here.
admin.site.register(State)
admin.site.register(City)
admin.site.register(BikeCompany)
admin.site.register(BikeModel)
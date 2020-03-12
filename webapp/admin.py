from django.contrib import admin
from . models import Employees, Managers

admin.site.register(Employees)
admin.site.register(Managers)
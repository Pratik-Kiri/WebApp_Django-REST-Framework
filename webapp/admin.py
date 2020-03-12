from django.contrib import admin
from . models import Employee, Manager, Project

admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Project)
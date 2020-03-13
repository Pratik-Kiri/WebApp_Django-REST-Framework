from django.contrib import admin
from . models import Employee, Manager, Project, Client

admin.site.register(Employee)
admin.site.register(Manager)
admin.site.register(Project)
admin.site.register(Client)
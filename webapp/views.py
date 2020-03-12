from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Employee, Manager, Project
from .serializers import EmployeeSerializer, ManagerSerializer, ProjectSerializer
from .permissions import EmployeePermission, ManagerPermission, ProjectPermission

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (EmployeePermission,)

class ManagerViewset(viewsets.ModelViewSet):
	queryset = Manager.objects.all()
	serializer_class = ManagerSerializer
	permission_classes = (ManagerPermission,)

class ProjectViewset(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer
	permission_classes = (ProjectPermission,)
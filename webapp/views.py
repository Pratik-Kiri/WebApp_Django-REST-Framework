from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Employees, Managers
from .serializers import EmployeeSerializer, ManagerSerializer
from .permissions import EmployeePermission, ManagerPermission

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (EmployeePermission,)

class ManagerViewset(viewsets.ModelViewSet):
	queryset = Managers.objects.all()
	serializer_class = ManagerSerializer
	permission_classes = (ManagerPermission,)
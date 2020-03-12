from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Employees
from .serializers import EmployeeSerializer
from .permissions import EmployeePermission

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (EmployeePermission,)
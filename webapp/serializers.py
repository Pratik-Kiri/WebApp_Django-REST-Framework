from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from .models import Employees, Managers

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employees
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Managers
        fields = '__all__'
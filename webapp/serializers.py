from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError
from .models import Employee, Manager, Project

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    project_manager_name = serializers.CharField(source='project_manager', read_only=True)
    
    class Meta:
        model = Project
        fields = ('name', 'start_date', 'project_manager', 'project_manager_name', 'allocated_hours', 'created_timestamp', 'updated_timestamp')
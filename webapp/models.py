from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
    	return self.first_name

class Managers(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    def __str__(self):
    	return self.first_name
from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
    	return self.first_name

class Manager(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    manager_id = models.IntegerField()

    def __str__(self):
    	return self.first_name

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    project_manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True,
                                        related_name="pro_managers",
                                        blank=True,
                                        verbose_name="project manager")
    allocated_hours = models.IntegerField(null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_timestamp = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
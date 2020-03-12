from rest_framework import routers
from django.conf.urls import url, include

from django.urls import path


app_name = 'webapp'

from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views

from .views import (

    EmployeeViewset,
)

app_name = 'webapp'
router = routers.DefaultRouter()

router.register(r'employees', EmployeeViewset)

urlpatterns = [
    url(r'', include(router.urls)),
]
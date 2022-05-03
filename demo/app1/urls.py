from django.urls import path
from .views import employeeView,employeedataView



urlpatterns = [


    path("emp/", employeeView, name="emp"),
    path("empdata/", employeedataView, name="empdata")



]
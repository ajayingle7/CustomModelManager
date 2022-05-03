from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.


def employeeView(request):
    template_name = "app1/employee.html"
    form = EmployeeForm()
    context = {"form":form}

    if request.method=="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()




    return render(request,template_name,context)


def employeedataView(request):
    template_name = "app1/data.html"
    obj = Employee.objects.get_ename_exclude("Ajay")
    context = {"data":obj}

    return render(request,template_name,context)


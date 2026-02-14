from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def dashboard(request):
    employees = Employee.objects.all()
    return render(request, 'dashboard.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})

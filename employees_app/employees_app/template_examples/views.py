from django.shortcuts import render

# Create your views here.
from employees_app.employees.models import Employee, Department


def index(request):
    employees = [e for e in Employee.objects.order_by('first_name')]
    context = {
        'number_1': 123,
        'number_2': 321,
        'number_3': 200,
        'numbers': [123, 321, 200],
        'title': 'Employees list',
        'employees': employees,
        #  'employees': Employee.objects.order_by('first_name').all(),
        'department_names': [d.name for d in Department.objects.all()],
    }
    return render(request, 'templates_examples/index.html', context)

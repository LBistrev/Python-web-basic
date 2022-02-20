import random
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.


# def home(request):
#     html = f'<h1>{request.method}: This is home</h1>'
#     # return HttpResponseNotFound()
#     return HttpResponse(
#         html,
#         content_type='text/html',
#         headers={
#             'x-lubo-header': 'Django'
#         },
#     )
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def home(request):
    print(reverse_lazy("index"))
    print(reverse_lazy("go to home"))
    print(reverse_lazy("list departments"))
    print(reverse_lazy("custom url"))
    print(reverse_lazy("department details", kwargs={
        'department_id': 9,
    }))
    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(15)]
    }
    return render(request, 'index.html', context, content_type='text/html')


def redirect_to_home(request):
    # return HttpResponseRedirect()
    # return redirect(to='/')
    # return redirect('department details', department_id=random.randint(1, 1024))
    return redirect('index')


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()


def department_details(request, department_id):
    return HttpResponse(f"This is department details: {department_id}")


def list_departments(request):
    # така създаваме обект
    department = Department(
        name=f'Department {random.randint(1, 1024)}',

    )
    # ако искаме да отиде в базата му казваме
    department.save()
    # същото можем да направим и като му кажем
    # Department.objects.create(
    #    name = f'Department {random.randint(1, 1024)}'
    # )
    context = {
        'departments': Department.objects
            .prefetch_related('employee_set')
            .all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create(request):
    return HttpResponse("created")

from django.shortcuts import render

import random

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

# Create your views here.


# def home(request):
#     html = f'<h1>{request.method}: This is home'
#     #return render(rand_num, rand_num)
#     return HttpResponse('fuck')


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    print(reverse_lazy('custom url'))
    print(reverse_lazy('department details', kwargs={
        'department_id': 15,
    }))
    context = {
        'number': random.randint(0, 1024),
        'numbers': [random.randint(0, 1024) for _ in range(16)],
    }

    return render(request, 'index.html', context)


def go_to_home(request):
    return redirect('department details', department_id=random.randint(1, 1024))  # home page or in our case localhost:8000


def not_found(request):
    raise Http404()


def department_details(request, department_id):
    return HttpResponse(f"This is department details {department_id} {type(request)}")


def list_departments(request):
    return HttpResponse("This is departments list")


def list_employees(request):
    return HttpResponse("This is employees list")


def create(request):
    return HttpResponse("Created")


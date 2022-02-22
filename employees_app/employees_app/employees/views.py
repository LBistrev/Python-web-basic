import random

from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms
from django.core import validators

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


# def home(request):
#     print(reverse_lazy("index"))
#     print(reverse_lazy("go to home"))
#     print(reverse_lazy("list departments"))
#     print(reverse_lazy("custom url"))
#     print(reverse_lazy("department details", kwargs={
#         'department_id': 9,
#     }))
#     context = {
#         'number': random.randint(0, 1024),
#         'numbers': [random.randint(0, 1024) for _ in range(15)]
#     }
#     return render(request, 'index.html', context, content_type='text/html')
#
#
# def redirect_to_home(request):
#     # return HttpResponseRedirect()
#     # return redirect(to='/')
#     # return redirect('department details', department_id=random.randint(1, 1024))
#     return redirect('index')
#
#
# def not_found(request):
#     # return HttpResponseNotFound()
#     raise Http404()
#
#
# def department_details(request, department_id):
#     return HttpResponse(f"This is department details: {department_id}")
#
#
# def list_departments(request):
#     # така създаваме обект
#     department = Department(
#         name=f'Department {random.randint(1, 1024)}',
#
#     )
#     # ако искаме да отиде в базата му казваме
#     department.save()
#     # същото можем да направим и като му кажем
#     # Department.objects.create(
#     #    name = f'Department {random.randint(1, 1024)}'
#     # )
#     context = {
#         'departments': Department.objects
#             .prefetch_related('employee_set')
#             .all(),
#         'employees': Employee.objects.all(),
#     }
#     return render(request, 'list_departments.html', context)
#
#
# def create(request):
#     return HttpResponse("created")

def validate_positive(value):
    if value < 0:
        raise ValidationError("Value must be positive")


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#     )
#     last_name = forms.CharField(
#         max_length=40,
#     )
#
#     egn = forms.CharField(
#         max_length=10,
#         validators=(
#             validators.MinLengthValidator(10),
#         )
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'QA Engineer'),
#             (1, 'DevOps Specialist'),
#         )
#     )
#
#     company = forms.ChoiceField(
#         choices=((c, c) for c in Employee.COMPANIES),
#     )

class EmployeeForm(forms.ModelForm):

    bot_catcher = forms.CharField(
        widget=forms.HiddenInput(),
        required=False,
    )

    def clean_bot_catcher(self):
        value = self.cleaned_data['bot_catcher']
        if value:
            raise ValidationError("This is a BOT!")

    class Meta:
        model = Employee
        #  fields = ('first_name', 'last_name')
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'},
            )
        }


class EditEmployeeForm(EmployeeForm):

    def clean(self):
        return super().clean()

    class Meta:

        model = Employee
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'},
            )
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
        ),
    )


def home(request):
    return render(request, 'index.html')


# def create_employee(request):
#     if request.method == "GET":
#         context = {
#             'employee_form': EmployeeForm(),
#         }
#         return render(request, 'create.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#         context = {
#             'employee_form': employee_form,
#         }
#         return render(request, 'create.html', context)


def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # save to Database
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     egn=employee_form.cleaned_data['egn'],
            #     company=employee_form.cleaned_data['company'],
            #     department_id=1,
            # )
            # # emp.save()
            # emp = Employee(
            #     # unpacked dictionary form
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            # emp.save()
            employee_form.save()
            return redirect('index')
    else:
        employee_form = EmployeeForm()

    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }

    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)

    if request.method == "POST":
        employee_form = EditEmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee')
    else:
        employee_form = EditEmployeeForm(instance=employee)

    context = {
        'employee': employee,
        'employee_form': employee_form
    }

    return render(request, 'edit.html', context)

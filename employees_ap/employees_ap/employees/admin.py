from django.contrib import admin

# Register your models here.
from employees_ap.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

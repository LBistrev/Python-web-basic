from django.contrib import admin

# Register your models here.
from django101.demo.models import Task

# Variant 1 for registration
# admin.site.register(Task)


# Variant 2
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

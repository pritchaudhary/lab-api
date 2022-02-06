from csv import list_dialects
from django.contrib import admin
from .models import Departments

# Register your models here.

class DepartmentsModel(admin.ModelAdmin):
    list_display=("id", "name")
    search_fields=["id", "name"]


admin.site.register(Departments, DepartmentsModel)

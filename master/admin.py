from atexit import register
# from csv import list_dialects
from django.contrib import admin
from .models import Departments, Doctor, Reason, Sampletype, Services, SubDepartments, Parameters, Titles
# Register your models here.


class DepartmentsModel(admin.ModelAdmin):
    list_display = ("name","is_active")
    search_fields = ["id", "name"]
    # readonly_fields = ("guid",)


class SubDepartmentsModel(admin.ModelAdmin):
    list_display = ("id", "name","shortdepName","barcodeprintflag","departments")
    search_fields = ["id", "name", "departments__name"]
    # readonly_fields = ("guid",)
    list_filter = ["name","shortdepName","barcodeprintflag",]
    autocomplete_fields = ("departments",)


class ParametersModel(admin.ModelAdmin):
    list_display = ("id", "name", "report_name", "unit", "rate", "method", "suffix",
                    "formulae", "dc", "precision", "default_status", "is_required")
    search_fields = ["id", "name", "report_name", "unit", "rate", "method", "suffix",
                     "formulae", "dc", "precision", "default_status", "is_required"]
    #list_filter = ["param_name"]

class SampletypeModel(admin.ModelAdmin):
    list_display = ("name","description","is_active")
    search_fields = ["id", "name"]
    # readonly_fields = ("guid",)

class TitlesModel(admin.ModelAdmin):
    list_display = ("title","disporder","gender")
    search_fields = ["id", "tiles"]
    # readonly_fields = ("guid",)


class ReasonModel(admin.ModelAdmin):
    list_display = ("reasontype","reasonflag")
    search_fields = ["id", "reasontype"]
    # readonly_fields = ("guid",)

class DoctorModel(admin.ModelAdmin):
    list_display = ("doctorname","mobileno")
    search_fields = ["id", "doctorname"]
    # readonly_fields = ("guid",)    


class ServicestypeModel(admin.ModelAdmin):
    list_display = ("services_name","report_name","rate","service_deptname","servicesmapcode","is_active")
    search_fields = ["id", "services_name"]
    # readonly_fields = ("guid",)
    autocomplete_fields = ("sampletype",)
    autocomplete_fields=("service_deptname",)

admin.site.register(Departments, DepartmentsModel)
admin.site.register(SubDepartments, SubDepartmentsModel)
admin.site.register(Parameters, ParametersModel)
admin.site.register(Sampletype, SampletypeModel)
admin.site.register(Services, ServicestypeModel)
admin.site.register(Titles,TitlesModel)
admin.site.register(Reason,ReasonModel)
admin.site.register(Doctor,DoctorModel)

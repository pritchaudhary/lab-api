from email.policy import default
from msilib import schema
from pkgutil import get_data
from pyexpat import model
from wsgiref.simple_server import demo_app
from django.db import models
import uuid
from django.db.models.query import QuerySet
from datetime import datetime

# Create your models here.


class Departments(models.Model):
    name = models.CharField(max_length=200, null=True)
    # creationid=models.CharField(max_length=200 ,null=True)
    # creationdate=models.DateField(default=datetime)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "departments"
        verbose_name = 'Departments'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name


class SubDepartments(models.Model):
    name = models.CharField(max_length=250)
    shortdepName = models.CharField(max_length=20, null=True)
    code = models.IntegerField(null=True)
    barcodeprintflag = models.BooleanField(default=True)
    emailflag = models.BooleanField(default=True)
    smsFlag = models.BooleanField(default=True)
    # creationid=models.CharField(max_length=200, null=True)
   # creationdate=models.DateField(default=datetime)
    departments = models.ForeignKey(
        Departments, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "sub_departments"
        verbose_name = 'Sub Departments'
        verbose_name_plural = 'Sub Departments'

    def __str__(self):
        return self.name

    # def __str__(self):
    #     if self.departments:
    #         return f"{self.id} - {self.departments}"
    #     return f"{self.id}"


class Parameters(models.Model):
    name = models.CharField(max_length=250, null=True)
    report_name = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=30)
    rate = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    method = models.CharField(max_length=30)
    suffix = models.CharField(max_length=2)
    formulae = models.CharField(max_length=100)
    dc = models.CharField(max_length=1)
    precision = models.IntegerField()
    default_status = models.CharField(max_length=1)
    # creationid=models.CharField(max_length=200, null=True)
    # creationdate=models.DateField(default=datetime)
    is_required = models.BooleanField(default=True)

    class Meta:
        db_table = "parameters"
        verbose_name = 'Parameters'
        verbose_name_plural = 'Parameters'

    # def __str__(self):
    #     return self.param_name


class Sampletype(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    # creationid=models.CharField(max_length=200,null=True)
    # creationdate=models.DateField(default=datetime)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "sampletype"
        verbose_name = 'Sampletype'
        verbose_name_plural = 'Sampletype'

    def __str__(self):
        return self.name


class Titles(models.Model):
    title = models.CharField(max_length=200)
    disporder = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    # creationid=models.CharField(max_length=200 ,null=True)
    # creationdate=models.DateField(default=datetime)

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Titles"
        verbose_name = 'Titles'
        verbose_name_plural = 'Titles'

    def __str__(self):
        return self.title


class Reason(models.Model):
    reasontype = models.CharField(max_length=200, null=True)
    reasonflag = models.CharField(max_length=200, null=True)
    # creationid=models.CharField(max_length=200 ,null=True)
    # creationdate=models.DateField(default=datetime)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Reason"
        verbose_name = 'Reason'
        verbose_name_plural = 'Reason'

    def __str__(self):
        return self.reasontype


class Doctor(models.Model):
    doctorname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    emailid = models.CharField(max_length=200)
    flagstatus = models.CharField(max_length=1)
    mobileno = models.IntegerField()
    reportmailflag = models.CharField(max_length=1)
    reportloginid = models.CharField(max_length=100)
    reportpass = models.CharField(max_length=100)
    intcode = models.CharField(max_length=100)
    # creationdate=models.DateField(default=datetime)
    lastmodifiedon = models.DateField()
    birthday = models.DateField()
    anniversarydate = models.DateField()
    licenseno = models.CharField(max_length=200)
    proname = models.CharField(max_length=200)
    # creationid=models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "Doctor"
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctor'

    def __str__(self):
        return self.doctorname


class Services(models.Model):
    services_name = models.CharField(max_length=250, null=True)
    report_name = models.CharField(max_length=100, unique=True)
    servicesmapcode = models.CharField(max_length=30)
    service_deptname = models.ForeignKey(
        SubDepartments, on_delete=models.SET_NULL, null=True)
    rate = models.DecimalField(null=True, max_digits=20, decimal_places=2)
    method = models.CharField(max_length=30)
    service_order = models.IntegerField()
    report_format = models.IntegerField()
    suppress_report_name = models.BooleanField(default=True)
    service_footer = models.CharField(max_length=250, null=True)
    service_outside = models.BooleanField(default=True)
    service_printtogether = models.BooleanField(default=True)
    service_web_flag = models.BooleanField(default=True)
    services_alias = models.CharField(max_length=30)
    services_days = models.IntegerField()
    critical_flag = models.BooleanField(default=True)
    sms_flag = models.BooleanField(default=True)
    color_code = models.CharField(max_length=30)
    sampletype = models.ForeignKey(
        Sampletype, on_delete=models.SET_NULL, null=True)
    disposalday = models.IntegerField()
    gendertype = models.CharField(max_length=6)
    specinstruction = models.CharField(max_length=250, null=True)
    patinstruction = models.CharField(max_length=250, null=True)
    techinstruction = models.CharField(max_length=250, null=True)
    question_flag = models.BooleanField(default=True)
    urgent_flag = models.BooleanField(default=True)
    lab_processtime = models.IntegerField()
    urgent_processtime = models.IntegerField()
    consent_flag = models.BooleanField(default=True)
    services_status = models.CharField(max_length=1)
    services_forhomecoll = models.BooleanField(default=True)
    ispdf_services = models.BooleanField(default=True)
    ismanual_services = models.BooleanField(default=True)
    gst_services = models.BooleanField(default=True)
    # creationid=models.CharField(max_length=200, null=True)
    # creationdate=models.DateField(default=datetime)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "services"
        verbose_name = 'Services'
        verbose_name_plural = 'services'

    def __str__(self):
        return self.services_name

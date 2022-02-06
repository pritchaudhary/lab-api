from django.shortcuts import render
from .serializers import DepartmentSerializer
from rest_framework import generics
from .models import Departments
# Create your views here.

class DepartmentsViews(generics.ListAPIView):
    serializer_class = DepartmentSerializer

    def get_queryset(self):

        queryset = Departments.objects.all()
        return queryset
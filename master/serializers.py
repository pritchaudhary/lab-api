from dataclasses import fields
from rest_framework import routers, serializers, viewsets
from .models import Departments

class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = Departments
        fields = ('__all__')
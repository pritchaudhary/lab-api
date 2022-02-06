from rest_framework import serializers
from .models import Departments, SubDepartments, Parameters


class DepartmentsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    is_active = serializers.BooleanField(required=True)

    class Meta:
        model = Departments
        fields = ('__all__')

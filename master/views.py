from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DepartmentsSerializer
from .models import Departments
from core_api.helpers import response_dict
from rest_framework import generics


class DepartmentsViews(generics.ListAPIView):
    serializer_class = DepartmentsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Departments.objects.all()
        department_id = self.request.query_params.get('department_id')
        if department_id is not None:
            queryset = queryset.filter(id=department_id)
        return queryset

    def post(self, request):
        serializer = DepartmentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        departments = self.get_object()
        serializer = DepartmentsSerializer(departments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            department_id = self.request.query_params.get('department_id')
            if not (department_id and Departments.objects.filter(id=department_id).exists()):
                response = response_dict(
                    data=None, error=True, message="Not Valid document id")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                instance = Departments.objects.get(id=department_id)
                instance.is_active = False
                instance.save()
                response = response_dict(
                    data=dict(id=department_id), error=True, message="Successfully deleted.")
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = response_dict(
                data=None, error=True, message=str(e.__str__()))
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

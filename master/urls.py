from django.urls import path
from .views import DepartmentsViews

urlpatterns = [
    path('department/', DepartmentsViews.as_view()),
    path('department/<int:pk>', DepartmentsViews.as_view()),
]

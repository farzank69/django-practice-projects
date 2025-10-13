from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/', views.read_student_api)
]

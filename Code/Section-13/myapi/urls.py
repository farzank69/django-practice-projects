from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_student),
    path('studentapi/', views.read_student_api)
]

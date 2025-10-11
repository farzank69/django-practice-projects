from django.urls import path
from . import views
urlpatterns = [
    path('list', views.student_list),
    path('list/<int:pk>', views.student_detail),

]

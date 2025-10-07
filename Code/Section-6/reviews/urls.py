from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),      # class based view.
    path('thank-you', views.thank_you, name='thank-you')
]






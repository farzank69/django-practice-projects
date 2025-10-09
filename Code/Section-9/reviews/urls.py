from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),      # class based view.
    path('thank-you', views.ThankYouView.as_view()),
    path('review', views.ReviewListView.as_view()),
    path('review-detail/<int:pk>', views.ReviewDetailView.as_view(), name='detail')
]






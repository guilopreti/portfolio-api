from django.urls import path

from . import views

urlpatterns = [
    path("front/", views.ListCreateView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path("fullstack/", views.ListCreateView.as_view()),
]

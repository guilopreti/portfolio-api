from django.urls import path

from . import views

urlpatterns = [
    path("back/", views.ListCreateView.as_view()),
]

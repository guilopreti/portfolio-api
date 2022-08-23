from django.urls import path

from . import views

urlpatterns = [
    path("techs/", views.ListCreateView.as_view()),
    path("techs/<pk>/", views.UpdateDeleteView.as_view()),
]

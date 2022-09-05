from django.urls import path

from . import views

urlpatterns = [
    path("fullstack/", views.ListCreateView.as_view()),
    path("fullstack/newest/", views.ListByDateView.as_view()),
    path("fullstack/<pk>/", views.UpdateDeleteView.as_view()),
    path("fullstack/del/<pk>/", views.RemoveTechView.as_view()),
    path("fullstack/add/<pk>/", views.AddTechView.as_view()),
]

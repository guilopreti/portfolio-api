from django.urls import path

from . import views

urlpatterns = [
    path("front/", views.ListCreateView.as_view()),
    path("front/newest/", views.ListByDateView.as_view()),
    path("front/<pk>/", views.UpdateDeleteView.as_view()),
    path("front/del/<pk>/", views.RemoveTechView.as_view()),
    path("front/add/<pk>/", views.AddTechView.as_view()),
]

from django.urls import path

from . import views

urlpatterns = [
    path("back/", views.ListCreateView.as_view()),
    path("back/newest/", views.ListByDateView.as_view()),
    path("back/<pk>/", views.UpdateDeleteView.as_view()),
    path("back/del/<pk>/", views.RemoveTechView.as_view()),
    path("back/add/<pk>/", views.AddTechView.as_view()),
]

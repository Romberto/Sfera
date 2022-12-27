from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.ApiUserView.as_view()),
    path('drivers/', views.ApiDriverView.as_view()),
    path('tokens/', views.ApiTokensView.as_view())
]
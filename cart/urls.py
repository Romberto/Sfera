from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.CartView.as_view(), name='cart')
]
from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.ProductCodView.as_view(), name='product_cod'),
]
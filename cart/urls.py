from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>/', views.CartView.as_view(), name='cart'),
    path('delete_product/', views.delete_item_product, name='delete_product'),
    path('cart_minus/', views.minus_item_product, name='minus__product'),
    path('cart_plus/', views.plus_item_product, name='plus__product'),
]
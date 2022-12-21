from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.db import models
from cart.models import CartModel, CartItemModel

# Create your views here.

class CartView(View):

    def get(self, request, id):
        try:
            cart = CartModel.objects.get(user=id)
            item_products = CartItemModel.objects.filter(cart=cart)
            data = {
                "cart": cart,
                "item_products": item_products
            }
        except CartModel.DoesNotExist :
            user = User.objects.get(id=id)
            cart = CartModel.objects.create(
                user=user
            )
            item_products = []
            if CartItemModel.objects.filter(cart=cart).exists():
                item_products = CartItemModel.objects.filter(cart=cart)
            data = {
                "cart": cart,
                "item_products": item_products
            }

        return render(request, 'cart/cart.html', data)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
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
        except CartModel.DoesNotExist:
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


def delete_item_product(request):
    id = request.GET.get('id_item_product')
    DasNotExist_error = False
    if CartItemModel.objects.filter(id=id).exists():
        CartItemModel.objects.get(id=id).delete()
    else:
        DasNotExist_error = True
    cart = CartModel.objects.get(user=request.user.id)
    summ = cart.total_price()
    data = {
        'summ': summ
    }
    return JsonResponse(data)


def minus_item_product(request):
    id = request.GET.get('id_item_product')
    item = CartItemModel.objects.get(id=id)

    if item.count == 1:
        item.delete()

    else:
        item.count = int(item.count) - 1
        item.save()
    cart = CartModel.objects.get(user=request.user.id)
    summ = cart.total_price()
    data = {
        'summ': summ
    }
    return JsonResponse(data)



def plus_item_product(request):
    id = request.GET.get('id_item_product')
    DasNotExist_error = False
    if CartItemModel.objects.filter(id=id).exists():
        item = CartItemModel.objects.get(id=id)
        item.count = int(item.count) + 1
        item.save()
    else:
        DasNotExist_error = True
    cart = CartModel.objects.get(user=request.user.id)
    summ = cart.total_price()
    data = {
        'summ': summ
    }
    return JsonResponse(data)
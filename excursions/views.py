from random import randint

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from cart.models import CartModel, CartItemModel
from excursions.models import ExcursionModel, ExcursionPointModel
from sendler import SendlerMessage

from django.contrib.auth import authenticate, login


class ExcursionsView(View):
    def get(self, request):
        excursions = ExcursionModel.objects.all()
        count = None
        if request.user.is_authenticated:
            cart = CartModel.objects.get(user=request.user.id)
            count = cart.total_count
        return render(request, 'excursions/excursions.html', {
            'excursions': excursions,
            'cart': count
        })


# Экскурсия return экскурсия по id
class ExcursionItemView(View):

    def get(self, request, id):
        excursion = ExcursionModel.objects.get(id=id)
        count_human = request.GET.get('count_human')
        return render(request, 'excursions/excur_item.html', {
            'excursion': excursion,
            'count_human': count_human
        })


class ExcursionCustomItem(View):
    def get(self, request, id, price):
        excursion = ExcursionModel.objects.get(id=id)


        return render(request, 'excursions/excur_item.html', {
            'excursion': excursion,
            'price': price
        })


class GalleryView(View):

    def get(self, request):
        points = ExcursionPointModel.objects.all()  # все точки экскурсий
        return render(request, 'excursions/excur_gallery.html', {
            'range': [1, 2, 3, 4, 5],
            'points': points
        })


class PointGalleryView(View):
    def get(self, request, id):
        point = ExcursionPointModel.objects.get(id=id)
        excursions = ExcursionModel.objects.filter(point__name=point.name)
        count = len(excursions)
        return render(request, 'excursions/point_gallery.html', {
            'point': point,
            'excursions': excursions,
            'count': count
        })


def clear_phone(phone):
    newTel = ''.join(filter(str.isdigit, phone))
    if str(newTel[0]) != '7':
        newTel = newTel.replace(newTel[0], '7', 1)

        return newTel
    else:
        return newTel


# генерация кода для подтверждения телефона
def checkPhone(request):
    phone = request.GET.get('phone')
    c_phone = clear_phone(phone)
    body = randint(1111, 9999)  # код для сверки телефона
    if User.objects.filter(username=c_phone).exists():
        user = User.objects.get(username=c_phone)
        user.set_password(str(body))
        user.save()
    else:
        user = User.objects.create_user(username=str(c_phone), password=str(body))
        cart = CartModel.objects.create(
            user=user
        )
        cart.save()
    data = {
        "code": body,
        "phone": phone
    }
    sendler = SendlerMessage()
    # sendler.send(phone, body)
    # todo срабатывает функция, которая отправляет СМС с кодом на номер {phone} код {body}
    print(f'срабатывает функция, которая отправляет СМС с кодом на номер {phone} код {body}')
    return JsonResponse(data)


def checkCode(request):
    code_input = request.GET.get('code')
    phone = request.GET.get('phone')
    c_phone = clear_phone(phone)
    user = authenticate(request, username=str(c_phone), password=str(code_input))
    if user:
        login(request, user)
        status = True
    else:
        status = False
    data = {
        'status': status
    }
    return JsonResponse(data)


def add_to_cart(request):
    try:
        id_exc = request.GET.get('id_exc')
        count = request.GET.get('count')
        custom_price = request.GET.get('custom_price')
        user = request.user.id
        cart = CartModel.objects.get(user=user)
        excursion = ExcursionModel.objects.get(id=id_exc)
        cart_row = CartItemModel.objects.filter(item=id_exc, cart=cart)
        if cart_row:
            if int(custom_price) > 1:        # если строка с кастомной ценой уже существует заменяем новой
                cart_row[0].custom_price = custom_price
                cart_row[0].save()
            else:
                cart_row[0].count = count
                cart_row[0].save()

        else:
            item_product = CartItemModel.objects.create(
                cart=cart,
                item=excursion,
                count=count,
                custom_price=custom_price
            )
            item_product.save()
            #todo после подключения виджета убрать cart.save()
        cart.save()
        success = True
    except Exception as _err:
        print(_err)
        success = False

    data = {
        'success': success
    }

    return JsonResponse(data)

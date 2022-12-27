from django.contrib import admin
from .models import CartModel, CartItemModel

class ItemInline(admin.StackedInline):
    model = CartItemModel
    extra = 4


class CartAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    list_display = ["user", "total_price", "paid"]


admin.site.register(CartModel, CartAdmin)

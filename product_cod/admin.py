from django.contrib import admin

from product_cod.models import ProductCodModel


# Register your models here.

class AdminProductCod(admin.ModelAdmin):
    list_display = ('body_cod', 'activate_driver', 'activated')

admin.site.register(ProductCodModel, AdminProductCod)

from django.contrib import admin
from .models import ExcursionModel, ExcursionPhoneCodModel, ExcursionPointModel


class AdminCart(admin.ModelAdmin):
    list_display = ('id', 'phone', 'random_cod', 'custom_price', 'human_count', 'excursions')

admin.site.register(ExcursionModel)
admin.site.register(ExcursionPhoneCodModel, AdminCart)
admin.site.register(ExcursionPointModel)

from django.contrib.auth.models import User
from django.db import models

from cart.models import CartModel
from drivers.models import DriverModel


# Create your models here.


class ProductCodModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activated = models.BooleanField(default=True)
    activate_driver = models.ForeignKey(DriverModel, on_delete=models.CASCADE, null=True, blank=True)
    date_activate = models.DateField(null=True, blank=True)
    body_cod = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Токен_код"
        verbose_name_plural = "Токены"

    def __str__(self):
        return str(self.body_cod)

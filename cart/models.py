from django.contrib.auth.models import User
from django.db import models
from excursions.models import ExcursionModel

class CartModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    total_sum = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    total_count = models.IntegerField(default=0, blank=True, null=True)

    def total_price(self):
        return sum([
            cart_item.total()
            for cart_item in CartItemModel.objects.filter(cart=self)
        ])

    def counts(self):
        return sum([
            cart_item.total_item()
            for cart_item in CartItemModel.objects.filter(cart=self)
        ])

    def save(self, *args, **kwargs):
        self.total_sum = self.total_price()
        self.total_count = self.counts()
        super(CartModel, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user}, {self.total_price()}: {self.paid}"



class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel, on_delete=models.CASCADE, null=True, blank=True)
    item = models.ForeignKey(ExcursionModel, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    custom_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def total(self):
        if self.custom_price:
            return self.custom_price
        else:
            return self.count * self.item.price

    def total_item(self):
        return self.count




    def __str__(self):
        return f"{self.item.name}, " \
               f"${self.item.price} * {self.count} = {self.total()}"


#cart_cartitemmodel

#cart_cartmodel
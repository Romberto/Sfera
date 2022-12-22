from django.db import models
from django.urls import reverse


def photo_file_name(instance, filename):
    return '/'.join(['exsursions', filename])


def map_file_name(instance, filename):
    return '/'.join(['exsursions', filename])


# Экскурсия
class ExcursionModel(models.Model):
    actual = models.BooleanField(default=True)  # актуальность
    name = models.CharField(max_length=200)  # название
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)  # цена
    description = models.TextField(blank=True, null=True)  # описание
    photo = models.FileField(upload_to=photo_file_name, null=True, blank=True)  # фото
    excursion_map = models.FileField(upload_to=map_file_name, null=True, blank=True)  # карта маршрута
    point = models.ManyToManyField('ExcursionPointModel')
    custom = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Экскурсия"
        verbose_name_plural = "Экскурсии"

    def __str__(self):
        return self.name


def content_excursion_name(instance, filename):
    return '/'.join(['exsursions_point', filename])


class ExcursionPointModel(models.Model):
    name = models.CharField(max_length=250)
    photo = models.FileField(upload_to=content_excursion_name, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Точка галереи"
        verbose_name_plural = "Точки галереи"

    def get_absolute_url(self):
        return reverse('point', kwargs={'id': self.id})

    def __str__(self):
        return self.name

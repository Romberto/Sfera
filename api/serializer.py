from django.contrib.auth.models import User
from rest_framework import serializers

from drivers.models import DriverModel
from product_cod.models import ProductCodModel


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverModel
        fields = '__all__'

class TokensListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCodModel
        fields = '__all__'
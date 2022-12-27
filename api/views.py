from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from drivers.models import DriverModel
from product_cod.models import ProductCodModel
from .serializer import UserListSerializer, DriverListSerializer, TokensListSerializer

class ApiUserView(APIView):


    def get(self, request):
        users=  User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class ApiDriverView(APIView):

    def get(self, request):
        drivers = DriverModel.objects.all()
        serializer = DriverListSerializer(drivers, many=True)
        return Response(serializer.data)

class ApiTokensView(APIView):
    def get(self,request):

        tokens = ProductCodModel.objects.all()
        serializer = TokensListSerializer(tokens, many=True)
        return Response(serializer.data)

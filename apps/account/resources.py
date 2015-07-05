# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import CustomUserSerializer 
from .models import CustomUser
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.hashers import make_password


class UserViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    """
        A viewset for Users
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    @list_route(methods=['POST'])
    def auth(self, request):
        return ObtainAuthToken().post(request)

    def create(self, request):        
        data = {
            "email": request.data.get('username'),
            "password": make_password(request.data.get('password')),
            "city": request.data.get('city'),
            "first_name":  request.data.get('first_name'),
            "last_name":  request.data.get('last_name')           
        }

        if CustomUser.objects.filter(email=data["email"]).exists():
            return Response({'username':"Username already exist"}, status=400)

        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()            
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

        
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import CustomUser
from django.conf import settings


class CustomUserSerializer(serializers.ModelSerializer):    
    class Meta:
        model = CustomUser         
        fields = ( 'id','password', 'city', 'first_name', 'last_name', 'email', )
        # fields = ( 'id', 'city', 'first_name', 'last_name', 'email','avatar', )


class CustomUserReadSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser         
        fields = ( 'id', 'city', 'first_name', 'last_name', 'email','avatar', )

    def get_avatar(self,obj):
        try:
            url = obj.avatar.url
            return url
        except ValueError, e:
            return settings.MEDIA_URL+'avatars/default.jpg'
        
    
        
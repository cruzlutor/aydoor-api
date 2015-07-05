# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = CustomUser         
        fields = ( 'id','password', 'city', 'first_name', 'last_name', 'email','avatar' )

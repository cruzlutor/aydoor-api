# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
    Service, Advert, Booking
)
from apps.account.serializers import CustomUserSerializer


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service


class AdvertSerializer(serializers.ModelSerializer):
    user_provider = CustomUserSerializer(many=False)
    service = ServicioSerializer(many=False)
    class Meta:
        model = Advert


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
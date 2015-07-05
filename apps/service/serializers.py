# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
    Service, Advert, Booking
)
from apps.account.serializers import CustomUserReadSerializer

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service


class AdvertSerializer(serializers.ModelSerializer):
    user_provider = CustomUserReadSerializer(many=False)
    service = ServicioSerializer(many=False)
    class Meta:
        model = Advert


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking


class BookingReadSerializer(serializers.ModelSerializer):
    user_provider = serializers.SerializerMethodField()
    user_client = CustomUserReadSerializer(many=False)
    service = serializers.SerializerMethodField()

    class Meta:
        model = Booking

    def get_user_provider(self, obj):
        return CustomUserReadSerializer(obj.advert.user_provider).data

    def get_service(self, obj):
        return ServicioSerializer(obj.advert.service).data
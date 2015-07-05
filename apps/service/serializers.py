# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
    Service, Advert, Booking
)


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service


class AdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (
    Service,
)


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service

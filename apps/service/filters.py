# -*- coding: utf-8 -*-
from .models import Service
import django_filters

class ServiceFilter(django_filters.FilterSet):    
    class Meta:
        model = Service
        fields = {
            'name': ['exact', 'icontains']         
        }
        order_by = ['name']
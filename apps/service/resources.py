# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ServicioSerializer, AdvertSerializer,
    BookingSerializer,
)
from .models import Service, Advert, Booking 
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route


class ServiceViewSet(
    mixins.CreateModelMixin,
    viewsets.GenericViewSet):
    """
        A viewset for services
    """
    queryset = Service.objects.all()
    serializer_class = ServicioSerializer


class AdvertViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """
        A view set for AdverViewsets
    """
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

    @list_route(methods=['GET'])
    def search(self, request):
        return Response({'data':'data'})


class BookingViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    # viewsets.ModelViewSet
    ):
    """
        Viewset for Bookings
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    @detail_route(methods=['POST'])
    def cancel(self, request, pk):
        return Response({'data':'data for cancel'})

    @detail_route(methods=['POST'])
    def accept(self, request, pk):
        return Response({'data':'data for accpet'})


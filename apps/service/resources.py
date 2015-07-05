# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    ServicioSerializer, AdvertSerializer,
    BookingSerializer, BookingReadSerializer
)
from .models import Service, Advert, Booking 
from rest_framework import viewsets, mixins
from rest_framework.decorators import detail_route, list_route
from django.shortcuts import get_object_or_404
from .filters import ServiceFilter
from rest_framework.permissions import AllowAny


class ServiceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """
        A viewset for services
    """
    queryset = Service.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = (AllowAny,)

    filter_class = ServiceFilter


    def list(self, request):
        return super(ServiceViewSet, self).list(request)


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
        services_pk = request.query_params.get('id_service', None)
        return Response({'data':'data'})
    
    def list(self, request):
        services_pk = request.query_params.get('id_service', None)
        if services_pk is not None:
            self.queryset = self.queryset.filter(service_id=services_pk)
        return super(AdvertViewSet, self).list(request)



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

    def retrieve(self, request, pk):        
        self.serializer_class =  BookingReadSerializer
        return super(BookingViewSet, self).retrieve(request, pk)

    @list_route(methods=['GET'])
    def filtered(self, request):
        self.queryset = self.queryset.filter(state__in=[Booking.REQUEST, Booking.ACCPETED])
        provider = request.query_params.get('provider', None) 
        
        if provider is not None:
            self.queryset = self.queryset.filter(advert__user_provider=request.user)
        else:            
            self.queryset = self.queryset.filter(user_client=request.user)
            
        serializer = BookingReadSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @detail_route(methods=['POST'])
    def cancel(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.state = Booking.CANCELED
        booking.save()
        return Response({'data':'ok'})

    @detail_route(methods=['POST'])
    def accept(self, request, pk):
        booking = get_object_or_404(Booking, pk=pk)
        booking.state = Booking.ACCPETED
        booking.save()
        return Response({'data':'ok'})


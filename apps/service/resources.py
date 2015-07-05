# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ServicioSerializer
from .models import Service
from rest_framework import viewsets


class SaiHi(APIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """           
        return Response({'hi':"hi mother fucher. .|."})



class ServiceViewSet(viewsets.ModelViewSet):
    """
        A viewset for clases
    """
    queryset = Service.objects.all()
    serializer_class = ServicioSerializer

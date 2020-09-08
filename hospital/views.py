from django.shortcuts import render
from .serializers import HospitalSerializer
from .models import Hospital
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from .serializers import HospitalSerializer

# Create your views here.

class HospitalViewSet(viewsets.ViewSet):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()
    permission_classes = (permissions.AllowAny,) 

    def list(self, request):
        queryset = Hospital.objects.all()
        serializer = HospitalSerializer(queryset, many=True)
        return Response(serializer.data)

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import HospitalSerializer
from .models import Hospital
from rest_framework import permissions

# Create your views here.

class HospitalListAPIView(ListCreateAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()
    permission_classes = (permissions.AllowAny,) #allowing everyone to see all registered hospital


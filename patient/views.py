from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PatientsSerializer, PatientsCardSerializer, PatientsDiagnosesSerializer
from .models import Patient, Card, Diagnoses
from rest_framework import permissions
from .permissions import IsOwner


# Patient ListViews
class PatientListAPIView(ListCreateAPIView):
    serializer_class = PatientsSerializer
    queryset = Patient.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,) 
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class PatientDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientsSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Patient.objects.all()
    lookup_field = "id"
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


# Card Views
class PatientCardListAPIView(ListCreateAPIView):
    serializer_class = PatientsCardSerializer
    queryset = Card.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,  )         
    def perform_create(self, serializer):
        return serializer.save(hospital=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(hospital=self.request.user)

class PatientCardDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientsCardSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Card.objects.all()
    lookup_field = "id"
    def get_queryset(self):
        return self.queryset.filter(hospital=self.request.user)


# Diagnoses Views
class PatientDiagnosesListAPIView(ListCreateAPIView):
    serializer_class = PatientsDiagnosesSerializer
    queryset = Diagnoses.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,) 
    def perform_create(self, serializer):
        return serializer.save(hospital=self.request.user)
    def get_queryset(self):
        return self.queryset.filter(hospital=self.request.user)

class PatientDiagnosesDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PatientsDiagnosesSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Diagnoses.objects.all()
    lookup_field = "id"
    def get_queryset(self):
        return self.queryset.filter(hospital=self.request.user)

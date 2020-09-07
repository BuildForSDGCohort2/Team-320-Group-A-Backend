from django.shortcuts import render

# Create your views here.
# api class generic
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from patient.models import HospitalHistory
from patient.serializers import PatientSerializer


class PatientsListView(generics.GenericAPIView, mixins.ListModelMixin,
                       mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = PatientSerializer
    queryset = HospitalHistory.objects.all()
    lookup_field = 'id'  # default lookup_field is our primary key bur to use something different

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request):

        return self.list(request)

    def post(self, request):
        return self.create(request)

class PatientDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin ):
    serializer_class = PatientSerializer
    queryset = HospitalHistory.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        return self.retrieve(request, id)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
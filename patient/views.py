from django.shortcuts import render

# Create your views here.
# api class generic
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from patient.models import HospitalHistory, Patient
from patient.serializers import PatientHospitalSerializer, PatientSerializer


# class PatientsListView(generics.GenericAPIView, mixins.ListModelMixin,
#                        mixins.CreateModelMixin):
#     serializer_class = PatientSerializer
#     queryset = HospitalHistory.objects.all()
#     lookup_field = 'id'  # default lookup_field is our primary key bur to use something different
#
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticated, IsAdminUser]
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)


class PatientHospitalDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin, ):
    serializer_class = PatientHospitalSerializer
    queryset = HospitalHistory.objects.all()
    lookup_field = 'code_no'

    def get(self, request, code_no, user=None):
        return self.list(request, code_no, user)

    # def put(self, request, id=None):
    #     return self.update(request, id)
    #
    # def delete(self, request, id=None):
    #     return self.destroy(request, id)


class PatientDetails(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = 'code_no'

    def get(self, request, code_no=None):
        return self.retrieve(request, code_no)

    # def put(self, request, id=None):
    #     return self.update(request, id)
    #
    # def delete(self, request, id=None):
    #     return self.destroy(request, id)

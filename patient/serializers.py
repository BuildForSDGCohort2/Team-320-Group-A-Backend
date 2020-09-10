from rest_framework import serializers
from patient.models import HospitalHistory, Diagnosis, Patient


class PatientHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalHistory
        fields = '__all__'


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = '__all__'



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

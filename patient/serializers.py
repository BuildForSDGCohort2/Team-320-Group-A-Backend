from rest_framework import serializers
from patient.models import HospitalHistory


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = HospitalHistory
        fields = '__all__'





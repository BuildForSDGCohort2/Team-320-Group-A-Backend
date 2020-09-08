from rest_framework import serializers
from .models import Patient, Card, Diagnoses


class PatientsSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Patient
        fields = ['id', 'name', 'phone', 'email', 'state','country']

class PatientsCardSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Card
        fields = ['id', 'name', 'card_number']

class PatientsDiagnosesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Diagnoses
        fields = ['id', 'sickness', 'note']


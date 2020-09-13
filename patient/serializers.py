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
        #     [
        #     'date_admitted',
        #     'code_no',
        #     'surname',
        #     'middle_name',
        #     'first_name',
        #     'phone_number',
        #     'email',
        #     'occupation',
        #     'gender',
        #     'Age',
        #     'dob',
        #     'marital_status',
        #     'blood_group',
        #     'genotype',
        #     'hospitals',
        #     'user'
        # ]
        user = serializers.ReadOnlyField(source='user.username')
        # print(repr(serializer))

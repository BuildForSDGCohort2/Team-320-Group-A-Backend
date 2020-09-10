from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospitalListAPIView.as_view(), name="hospital"),
    path('Create&ViewPatientHealthBill/', views.PatientsHospitalListView.as_view(), name="Create&ViewPatientHealthBill"),
    path('patientCreate/', views.PatientsListView.as_view(), name="patientCreate&list"),
    path('PatientHealthBillDetails/<int:pk>/', views.PatientHospitalDetails.as_view(), name="PatientHealthBilldetails"),
    path('patientDetails/<int:pk>/', views.PatientDetails.as_view(), name="patientdetails")
]

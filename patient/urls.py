from django.urls import path
from . import views


urlpatterns = [
    # path('hospitalhistory/', views.PatientsListView.as_view(), name="PatientList"),
    path('PatientHealthBillDetails/<str:code_no>/', views.PatientHospitalDetails.as_view(), name="HealthBill"), #healthbill
    path('patientDetails/<str:code_no>/', views.PatientDetails.as_view(), name="PatientDetail") #personal Details
]

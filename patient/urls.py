from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatientListAPIView.as_view(), name="patient"),
    path('<int:id>', views.PatientDetailAPIView.as_view(), name="patient"),
    path('card', views.PatientCardListAPIView.as_view(), name="card"),
    path('card/<int:id>', views.PatientCardDetailAPIView.as_view(), name="card"),
    path('diagnoses', views.PatientDiagnosesListAPIView.as_view(), name="diagnoses"),
    path('diagnoses/<int:id>', views.PatientDiagnosesDetailAPIView.as_view(), name="diagnoses")

]

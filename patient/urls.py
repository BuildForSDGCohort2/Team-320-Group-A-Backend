from django.urls import path
from . import views


urlpatterns = [
    path('', views.PatientsListView.as_view(), name="PatientList"),
    path('<int:id>/', views.PatientDetails.as_view(), name="PatientDetail")
]

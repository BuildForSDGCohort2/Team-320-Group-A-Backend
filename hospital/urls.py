from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospitalListAPIView.as_view(), name="hospital")
]

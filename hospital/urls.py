from django.urls import path
from . import views
from rest_framework import routers
from .views import HospitalViewSet

router = routers.DefaultRouter()
router.register('hospital', HospitalViewSet)

urlpatterns = router.urls

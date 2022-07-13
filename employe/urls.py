from django.urls import path, include
from rest_framework import routers
from .views import EmployeViewSet
router = routers.DefaultRouter()

router.register(r'employe',EmployeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
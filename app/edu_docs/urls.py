from django.urls import path, include
from rest_framework import routers

from .views import PlanViewSet, WordViewSet

router = routers.DefaultRouter()
router.register(r"plans", PlanViewSet, basename='plans')
router.register(r"", WordViewSet, basename='document')

urlpatterns = [
    path('', include(router.urls)),
]

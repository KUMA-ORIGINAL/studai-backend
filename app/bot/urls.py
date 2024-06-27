from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bot.views import PaymentCreateViewSet

router = DefaultRouter()

router.register(r'',
                PaymentCreateViewSet,
                basename='payments-create')

urlpatterns = [
    path('', include(router.urls)),
]
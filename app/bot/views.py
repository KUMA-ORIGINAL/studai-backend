from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response

from bot.handlers.main_2 import send_receipt_to_admin
from bot.handlers.main import bot
from bot.models import Payment
from bot.serializers import PaymentCreateSerializer


@extend_schema(tags=['Payments'])
@extend_schema_view(
    create=extend_schema(
        summary='Загрузка чека'
    ),
)
class PaymentCreateViewSet(viewsets.GenericViewSet,
                           generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            # Отправка чека в телеграм
            send_receipt_to_admin(payment=payment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

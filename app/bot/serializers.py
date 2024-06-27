from rest_framework import serializers

from bot.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Payment
        fields = '__all__'

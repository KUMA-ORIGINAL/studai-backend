from djoser.serializers import UserCreateSerializer, UserSerializer

from account.models import User


class UserCreateSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')


class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'first_name', 'last_name', 'photo')

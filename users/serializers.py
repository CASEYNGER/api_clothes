from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

from .models import CustomUser


class UserRegSerializer(UserCreateSerializer):
    """
    Кастомный сериализатор модели пользователя.

    Наследуется от UserCreateSerializer, который
    используется Djoser для регистрации нового пользователя.
    """

    class Meta(UserCreateSerializer.Meta):
        """
        Настройки поведения сериализатора.
        """
        model = CustomUser
        fields = (
            'id', 'username', 'password',
            'email', 'phone'
        )

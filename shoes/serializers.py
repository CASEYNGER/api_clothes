from rest_framework import serializers

from .models import Shoes


class ShoesSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели обуви.

    Наследуется от ModelSerializer, который автоматически создает
    сериализатор на основе модели Shoes.
    """

    class Meta:
        """
        Настройки поведения сериализатора.

        - работает с моделью Shoes.
        - все поля модели Shoes преобразуются в сериализуемые
        поля.
        """

        model = Shoes
        fields = '__all__'

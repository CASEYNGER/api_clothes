from rest_framework import serializers

from .models import Cloth


class ClothSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели одежды.

    Наследуется от ModelSerializer, который автоматически создает
    сериализатор на основе модели Cloth.
    """

    class Meta:
        """
        Настройки поведения сериализатора.

        - работает с моделью Cloth.
        - все поля модели Cloth преобразуются в сериализуемые
        поля.
        """

        model = Cloth
        fields = '__all__'

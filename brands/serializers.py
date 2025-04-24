from rest_framework import serializers

from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели бренда.

    Наследуется от ModelSerializer, который автоматически создает
    сериализатор на основе модели Brand.
    """

    class Meta:
        """
        Настройки поведения сериализатора.

        - работает с моделью Brand.
        - все поля модели Brand преобразуются в сериализуемые
        поля.
        """

        model = Brand
        fields = '__all__'

from rest_framework import viewsets, permissions

from .models import Cloth, Shoes
from .serializers import ClothSerializer, ShoesSerializer
from .permissions import CanAddClothPermission


class ClothViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели Cloth.

    Наследник ModelViewSet, который предоставляет все
    стандартные CRUD-действия для работы с моделями.
    """

    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CanAddClothPermission
    )
    filter_fields = (
        'color', 'cloth_type', 'size', 'gender',
        'brand', 'category'
    )


class ShoesViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели Shoes.

    Наследник ModelViewSet, который предоставляет все
    стандартные CRUD-действия для работы с моделями.
    """

    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CanAddClothPermission
    )
    filter_fields = (
        'color', 'shoes_type', 'size', 'gender', 'material'
    )

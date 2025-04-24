from rest_framework import viewsets, permissions

from .models import Shoes
from .serializers import ShoesSerializer
from api.permissions import CanAddClothPermission


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

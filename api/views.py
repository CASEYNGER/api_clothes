from rest_framework import viewsets, permissions, filters

from .models import Cloth
from .serializers import ClothSerializer
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
    filter_fields = ('color', 'cloth_type', 'size', 'gender')

from rest_framework import viewsets, permissions

from .models import Brand
from .serializers import BrandSerializer
from api.permissions import CanAddClothPermission


class BrandViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели Shoes.

    Наследник ModelViewSet, который предоставляет все
    стандартные CRUD-действия для работы с моделями.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        CanAddClothPermission
    )
    filter_fields = ('name',)

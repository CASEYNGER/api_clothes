from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import ClothViewSet


router_v1 = DefaultRouter()
router_v1.register(r'clothes', ClothViewSet)

urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
]

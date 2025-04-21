from django.urls import include, path

from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from .views import ClothViewSet


router_v1 = DefaultRouter()
router_v1.register(r'clothes', ClothViewSet)

urlpatterns = [
    path('api/v1/', include(router_v1.urls)),

    path(
        'api/v1/schema/',
        SpectacularAPIView.as_view(),
        name='schema'
    ),
    path(
        'api/v1/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
    path(
        'api/v1/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
]

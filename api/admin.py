from django.contrib import admin

from api.models.clothes import (
    Cloth, ClothType, ClothesSize
)
from api.models.shoes import (
    Shoes, ShoesMaterial, ShoesSize, ShoesType
)
from api.models.common import Gender, Color
from api.models.brand import Brand, Category


class ClothAdmin(admin.ModelAdmin):
    """Регистрация модели в админке."""

    list_display = ('title', 'article', 'cloth_type', 'size', 'gender')
    list_filter = ('cloth_type', 'size', 'gender')
    search_fields = ('title', 'brand', 'article', 'size', 'gender')
    fieldsets = (
        (
            'Основные данные', {
                'fields': (
                    'title', 'description', 'brand', 'article',
                    'price', 'category'
                ),
            }
        ),
        (
            'Тип и характеристики', {
                'fields': ('cloth_type', 'color', 'size', 'gender'),
            }
        ),
        (
            'Изображение', {
                'fields': ('image',),
            }
        ),
        (
            'Доступность', {
                'fields': ('is_available', 'is_published')
            }
        )
    )


class ShoesAdmin(admin.ModelAdmin):
    """Регистрация модели в админке."""

    list_display = ('title', 'brand', 'category', 'size', 'gender')
    list_filter = ('brand', 'size', 'category')
    search_fields = ('title', 'brand', 'size', 'article')
    fieldsets = (
        (
            'Основные данные', {
                'fields': (
                    'title', 'description', 'brand', 'article',
                    'price', 'category'
                ),
            }
        ),
        (
            'Тип и характеристики', {
                'fields': (
                    'shoes_type', 'color', 'size', 'gender',
                    'material'
                ),
            }
        ),
        (
            'Изображение', {
                'fields': ('image',),
            }
        ),
        (
            'Доступность', {
                'fields': ('is_available', 'is_published')
            }
        )
    )


admin.site.register(Cloth, ClothAdmin)
admin.site.register(ClothType)
admin.site.register(Color)
admin.site.register(ClothesSize)
admin.site.register(Gender)

admin.site.register(Shoes, ShoesAdmin)
admin.site.register(ShoesMaterial)
admin.site.register(ShoesSize)
admin.site.register(ShoesType)

admin.site.register(Brand)
admin.site.register(Category)

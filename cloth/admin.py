from django.contrib import admin

from .models import Cloth, ClothType, ClothesSize


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


admin.site.register(Cloth, ClothAdmin)
admin.site.register(ClothType)
admin.site.register(ClothesSize)

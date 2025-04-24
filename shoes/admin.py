from django.contrib import admin

from .models import Shoes, ShoesMaterial, ShoesSize, ShoesType


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


admin.site.register(Shoes, ShoesAdmin)
admin.site.register(ShoesMaterial)
admin.site.register(ShoesSize)
admin.site.register(ShoesType)

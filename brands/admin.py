from django.contrib import admin

from .models import Brand, Category


class BrandAdmin(admin.ModelAdmin):
    """Регистрация модели в админке."""

    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Brand, BrandAdmin)
admin.site.register(Category)

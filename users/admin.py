from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Регистрация модели в админке."""

    list_display = (
        'username', 'email', 'phone',
        'first_name', 'last_name', 'is_staff',
        'is_superuser'
    )
    search_fields = ('username', 'email', 'phone')


admin.site.register(CustomUser, CustomUserAdmin)

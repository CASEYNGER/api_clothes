from django.contrib import admin

from .models import Cloth, ClothType, Color, ClothesSize, Gender

admin.site.register(Cloth)
admin.site.register(ClothType)
admin.site.register(Color)
admin.site.register(ClothesSize)
admin.site.register(Gender)

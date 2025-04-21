from django.db import models


class Gender(models.Model):
    """Модель гендерной принадлежности."""

    name = models.CharField(max_length=20, verbose_name='Пол')

    def __str__(self):
        """Строковое представление для модели."""
        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'


class Color(models.Model):
    """Модель цвета одежды."""

    name = models.CharField(max_length=30, verbose_name='Цвет')

    def __str__(self):
        """Строковое представление для модели."""
        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

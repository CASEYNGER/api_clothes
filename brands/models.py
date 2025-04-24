from django.db import models


class Brand(models.Model):
    """Модель бренда."""

    name = models.CharField(
        max_length=100,
        verbose_name='Бренд',
        help_text='Введите название бренда.',
        unique=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Введите описание бренда.'
    )

    def __str__(self):
        """Строковое представление для модели."""

        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Category(models.Model):
    """Модель категории."""

    name = models.CharField(
        max_length=100,
        verbose_name='Категория',
        help_text='Введите название категории.',
        unique=True
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание',
        help_text='Введите описание категории.'
    )

    def __str__(self):
        """Строковое представление для модели."""

        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

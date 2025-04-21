from django.db import models

from api.validators import validate_cloth_price, validate_article
from .common import Color, Gender
from .brand import Brand, Category
from .mixins import TimeStampedMixin, PublishableMixin


class ShoesType(models.Model):
    """Модель типа обуви."""

    name = models.CharField(max_length=50, verbose_name='Тип')
    description = models.TextField(
        blank=True, verbose_name='Описание', default=''
    )

    def __str__(self):
        """Строковое представления для модели."""

        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Тип обуви'
        verbose_name_plural = 'Типы обуви'


class ShoesSize(models.Model):
    """Модель размера обуви."""

    code = models.CharField(max_length=10, verbose_name='Код', unique=True)
    label = models.CharField(max_length=10, verbose_name='Название')

    def __str__(self):
        """Строковое представление для модели."""

        return self.label

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Размер обуви'
        verbose_name_plural = 'Размеры обуви'


class ShoesMaterial(models.Model):
    """Модель материала обуви."""

    name = models.CharField(
        max_length=50,
        verbose_name='Основной материал'
    )

    def __str__(self):
        """Строковое представление для модели."""

        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Материал обуви'
        verbose_name_plural = 'Материалы обуви'


class Shoes(TimeStampedMixin, PublishableMixin):
    """Модель обуви."""

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Введите название обуви (не более 255 символов.)',
        verbose_name='Название',
    )
    description = models.TextField(
        null=False,
        help_text='Введите описание.',
        verbose_name='Описание'
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Бренд',
        help_text='Укажите бренд одежды.'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Категория',
        help_text='Укажите категорию.'
    )
    article = models.IntegerField(
        validators=[validate_article],
        unique=True,
        help_text='Введите артикул обуви.',
        verbose_name='Артикул',
    )
    shoes_type = models.ForeignKey(
        ShoesType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите тип обуви.',
        verbose_name='Тип обуви',
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите цвет обуви.',
        verbose_name='Цвет',
    )
    size = models.ForeignKey(
        ShoesSize,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите размер обуви.',
        verbose_name='Размер',
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите, для какого пола обувь.',
        verbose_name='Пол',
    )
    material = models.ForeignKey(
        ShoesMaterial,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите материал обуви.',
        verbose_name='Материал'
    )
    image = models.ImageField(
        upload_to='clothes/',
        blank=True,
        null=True,
        help_text='Добавьте изображение обуви.',
        verbose_name='Изображение',
    )
    price = models.IntegerField(
        null=False,
        help_text='Введите стоимость товара в рублях.',
        verbose_name='Цена',
        validators=[validate_cloth_price],
    )

    def __str__(self):
        """Строковое представление для модели."""

        return self.title

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'

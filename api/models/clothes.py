from django.db import models

from api.validators import validate_cloth_price, validate_article
from .common import Color, Gender
from .brand import Brand, Category
from .mixins import TimeStampedMixin, PublishableMixin


class ClothType(models.Model):
    """Модель типа одежды."""

    name = models.CharField(max_length=50, verbose_name='Тип')
    description = models.TextField(
        blank=True, verbose_name='Описание', default=''
    )

    def __str__(self):
        """Строковое представления для модели."""

        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Тип одежды'
        verbose_name_plural = 'Типы одежды'


class ClothesSize(models.Model):
    """Модель размеров одежды."""

    code = models.CharField(max_length=10, verbose_name='Код', unique=True)
    label = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        """Строковое представление для модели."""

        return self.label

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class Cloth(TimeStampedMixin, PublishableMixin):
    """Модель одежды."""

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Введите название элемента одежды (не более 255 символов.)',
        verbose_name='Название',
    )
    description = models.TextField(
        blank=True, help_text='Введите описание.', verbose_name='Описание'
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
        help_text='Введите артикул элемента одежды.',
        verbose_name='Артикул',
    )
    cloth_type = models.ForeignKey(
        ClothType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите тип одежды.',
        verbose_name='Тип одежды',
    )
    color = models.ForeignKey(
        Color,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите цвет одежды.',
        verbose_name='Цвет',
    )
    size = models.ForeignKey(
        ClothesSize,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите размер одежды.',
        verbose_name='Размер',
    )
    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text='Укажите, для какого пола элемент одежды.',
        verbose_name='Пол',
    )
    image = models.ImageField(
        upload_to='clothes/',
        blank=True,
        null=True,
        help_text='Добавьте изображение элемента одежды.',
        verbose_name='Изображение',
    )
    price = models.IntegerField(
        null=False,
        help_text='Введите стоимость товара в рублях.',
        verbose_name='Цена',
        validators=[validate_cloth_price],
    )

    def __str__(self):
        """Строковое представления для модели."""

        return self.title

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

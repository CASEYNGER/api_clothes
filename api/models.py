from django.db import models
from django.contrib.auth.models import User

from .validators import validate_cloth_price, validate_article


class ClothType(models.Model):
    """Модель типа одежды."""

    name = models.CharField(max_length=50, verbose_name='Тип')
    description = models.TextField(blank=True, verbose_name='Описание', default='')

    def __str__(self):
        """Строковое представления для модели."""
        return self.name

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Тип одежды'
        verbose_name_plural = 'Типы одежды'


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


class TimeStampedModel(models.Model):
    """Кастомная модель для времени создания или обновления товара."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Флаг абстракции."""

        abstract = True


class Cloth(TimeStampedModel):
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
        """Строковое представление для модели."""
        return self.title

    class Meta:
        """Оформление модели в админке."""

        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

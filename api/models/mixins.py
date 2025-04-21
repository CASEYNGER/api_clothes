from django.db import models


class TimeStampedMixin(models.Model):
    """Миксин для времени создания или обновления товара."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Флаг абстракции.

        Благодаря ему не создает новую таблицу в БД.
        """


class PublishableMixin(models.Model):
    """Миксин для добавления флагов публикации и доступности."""

    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликовано',
        help_text='Отображается ли товар на сайте.'
    )
    is_available = models.BooleanField(
        default=False,
        verbose_name='В наличии',
        help_text='Можно ли купить этот товар.'
    )

    class Meta:
        """
        Флаг абстракции.

        Благодаря ему не создает новую таблицу в БД.
        """

        abstract = True

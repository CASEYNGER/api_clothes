from django.core.exceptions import ValidationError


def validate_cloth_price(value):
    """Валидирует цену товара."""
    if value < 500:
        raise ValidationError('Слишком низкая цена. Минимум — 500.')
    if value > 500000:
        raise ValidationError('Слишком высокая цена. Максимум — 500 000.')


def validate_article(value):
    """Валидирует артикул товара."""
    str_value = str(value)

    if len(str_value) < 10:
        raise ValidationError(
            'Слишком короткий артикул. '
            'Он должен содержать минимум 10 символов.'
        )
    elif len(str_value) > 10:
        raise ValidationError(
            'Слишком длинный артикул. '
            'Он должен содержать максимум 10 символов.'
        )
    elif not str_value.isdigit():
        raise ValidationError('Артикул должен содержать только цифры.')

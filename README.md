# REST API для магазина одежды
(E-commerce project) REST API и настроенная панель администратора для работы с магазином одежды, предоставляющие возможность выполнять CRUD-операции с ассортиментом товаров.

## Стэк:
- Язык программирования: Python 3
- Фреймворк: Django 4.2.20
- Django REST Framework: 3.16.0
- Библиотека для аутентификации и авторизации: djoser 2.3.1
- База данных: SQLite (по умолчанию)
- Pillow

## Основные фичи
- Каталог одежды и обуви.
- Система брендов и категорий.
- Кастомная модель пользователя.
- Панель администратора.
- Корзина (в процессе).

## Начало работы с API
### 1. Клонируйте репозиторий на свой компьютер
```bash
git clone https://github.com/CASEYNGER/api_clothes
```

### 2. Создайте и активируйте виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv/Scripts/activate
```

### 3. Установите зависимости из файла `requirements.txt`
```bash
pip install -r requirements.txt
```

### 4. Выполните миграции базы данных
```bash
python manage.py migrate
```

### 5. Создайте суперпользователя для доступа в панель администратора
```bash
python manage.py createsuperuser
```

После этого вы сможете войти в административную панель по адресу:
```arduino
http://127.0.0.1:8000/admin/
```

### 6. Запуск сервера разработки
```bash
python manage.py runserver
```

## Эндпоинты документации к API
- *Схема*
`GET /api/v1/schema/`

- *ReDoc*
`GET /api/v1/redoc/`

- *Docs*
`GET /api/v1/docs/`

## Пагинация
По умолчанию используется пагинация с 5 объектами на страницу. Параметры пагинации можно передавать через URL:

- `GET /api/v1/clothes/?page=1` - Получить первую страницу.
- `GET /api/v1/clothes/?page=2` - Получить вторую страницу.

## Примечания
1. Для работы с изображениями, не забудьте настроить MEDIA_URL и MEDIA_ROOT в настройках Django. Также убедитесь, что у вас установлен пакет Pillow для работы с изображениями.
2. JWT токены предоставляют безопасную аутентификацию для работы с API. Вы можете использовать их для доступа к защищенным эндпоинтам.
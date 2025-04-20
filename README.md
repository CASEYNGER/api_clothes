# REST API для магазина одежды
REST API и настроенная панель администратора для работы с магазином одежды, предоставляющие возможность выполнять CRUD-операции с ассортиментом товаров.

## Стэк:
- Язык программирования: Python 3
- Фреймворк: Django 4.2.20
- Django REST Framework: 3.16.0
- Библиотека для аутентификации и авторизации: djoser 2.3.1
- База данных: SQLite (по умолчанию)

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
python manage.py makemigrations
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

## Эндпоинты API
- *Регистрация нового пользователя*
`POST /auth/users/`

Тело запроса:
```json
{
  "username": "example_user",
  "password": "example_password",
  "email": "user@example.com"
}
```

- *Получение JWT токена (логин)*
`POST /auth/jwt/create/`

Тело запроса:
```json
{
  "username": "example_user",
  "password": "example_password"
}
```

Пример ответа:
```json
{
  "access": "access_token",
  "refresh": "refresh_token"
}
```

- *Обновление токена*
`POST /auth/jwt/refresh/`

Тело запроса:
```json
{
  "refresh": "refresh_token"
}
```

- *Проверка токена*
`POST /auth/jwt/verify/`

Тело запроса:
```json
{
  "token": "access_token"
}
```

## Эндпоинты для работы с контентом
- *Получение списка товаров*
`GET /api/v1/clothes/`

Пример ответа:
```json
[
  {
    "id": 1,
    "title": "Футболка",
    "description": "Белая футболка с логотипом",
    "article": "1234567890",
    "price": 500,
    "color": 1,
    "cloth_type": 2,
    "size": 3,
    "gender": 1,
    "image": "/media/clothes/shirt.jpg"
  },
  ...
]
```

- *Получить товар по ID*
`GET /api/v1/clothes/{id}/`

Пример запроса:
```bash
GET /api/v1/clothes/1/
```

### Фильтрация товаров
Вы можете фильтровать товары по различным параметрам:
- по цвету: `GET /api/v1/clothes/?color=1`
- по размеру: `GET /api/v1/clothes/?size=1`
- по типу: `GET /api/v1/clothes/?cloth_type=1`
- по гендерной принадлежности: `GET /api/v1/clothes/?gender=1`

### Создание нового товара
`POST /api/v1/clothes/`

Пример запроса:
```json
{
  "title": "Футболка с принтом",
  "description": "Черная футболка с принтом на груди",
  "article": "9876543210",
  "price": 700,
  "color": 1,
  "cloth_type": 2,
  "size": 1,
  "gender": 1,
  "image": "/media/clothes/tshirt.jpg"
}
```

### Обновление товара
`PUT /api/v1/clothes/{id}/`

Пример запроса:
```json
{
  "title": "Обновленная футболка",
  "description": "Футболка с новыми характеристиками",
  "article": "1234567890",
  "price": 750,
  "color": 2,
  "cloth_type": 3,
  "size": 1,
  "gender": 1,
  "image": "/media/clothes/updated_tshirt.jpg"
}
```

### Удаление товара
`DELETE /api/v1/clothes/{id}/`

Пример запроса:
```bash
DELETE /api/v1/clothes/1/
```

## Пагинация
По умолчанию используется пагинация с 5 объектами на страницу. Параметры пагинации можно передавать через URL:

- `GET /api/v1/clothes/?page=1` - Получить первую страницу.
- `GET /api/v1/clothes/?page=2` - Получить вторую страницу.

## Примечания
1. Для работы с изображениями, не забудьте настроить MEDIA_URL и MEDIA_ROOT в настройках Django. Также убедитесь, что у вас установлен пакет Pillow для работы с изображениями.
2. JWT токены предоставляют безопасную аутентификацию для работы с API. Вы можете использовать их для доступа к защищенным эндпоинтам.
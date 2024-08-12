### проект «API-blog»

### 1. Описание проекта:
API-blog - это REST API для блог-платформы . Позволяет пользователям публиковать свои посты и управлять подписками через программный интерфейс взаимодействия.

### 2. Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Den4u/api_blog.git
```

```
cd api_blog
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### 3. Примеры:

Авторизированному пользователю необходимо получить токен, для этого нужно выполнить POST-запрос /api/v1/jwt/create/ передав поля username и password созданного пользователя.

При отправке запроса авторизированного пользователя передайте токен в заголовке Authorization: Bearer <токен>

/api/v1/posts/ (GET, POST, PUT, PATCH, DELETE)

/api/v1/posts/{post_id}/comments/ (GET, POST, PUT, PATCH, DELETE)

/api/v1/groups/ (GET)

/api/v1/follow/ (GET, POST)

### Автор проекта: https://github.com/Den4u

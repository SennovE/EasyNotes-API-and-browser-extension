# EasyNotes

Веб сервис, который позволяет сохранять заметки с комментариями.

API сделано на основе библиотеки `FastAPI` и `sqlalchemy` для работы с базой данных. Для сохранения конфеденциальности пользователей используется хэширование пароля в хранилище, а также OAuth2 схема при передаче пароля и аутентификация по JWT токену. Все обращения к базе данных происходят в ассинхронных функциях. Данные валидируются при помощи аннотации и схем с ипользованием `pydantic`.

## Функциональность

### Пользователь

---

**Регистрация**
```http
POST /api/v1/user/register
```

Параметры запроса:
- `username`: `string` `>= 5 characters` `matches ^\S+$`
- `password`: `string` `>= 8 characters`

---

**Аутентификация**
```http
POST /api/v1/user/token
```

Параметры запроса:
- `username`: `string`
- `password`: `string`

При успешной аутентификиции сервис вернет JWT-токен.

---

### Заметки

---

**При всех запросах связанных с заметками в headers надо передавать:**
```json
{"Authorization": "Bearer <JWT-токен, который был получен при аутентификации>"}
```

---

**Создание заметки**
```http
POST /api/v1/note
```

Параметры запроса:
- `title`: `string`
- `url`: `string | null` `HttpUrl`
- `note_text`: `string`
- `comment`: `string | null`
- `tag`: `string | null`

---

**Удаление заметки по названию**
```http
DELETE /api/v1/note
```
Параметры пути:
- `note_title`: `string`

---

**Изменение полей заметки**
```http
PUT /api/v1/note
```

Параметры пути:
- `note_title`: `string`

Параметры запроса:
- `title`: `string | null`
- `url`: `string | null` `HttpUrl`
- `note_text`: `string | null`
- `comment`: `string | null`
- `tag`: `string | null`

---

**Получение заметки по названию**
```http
GET /api/v1/note
```

Параметры пути:
- `note_title`: `string`

При передаче существующего названия будет выдана заметка с полями:
- `title`
- `url`
- `note_text`
- `comment`
- `tag`
- `date_created`

---

## Запуск

Требования:
- Python 3.11
- Poetry
- Docker
- Docker-compose

Перед запуском создайте файл с названием `.env`, в котором будут лежать параметры окружения.

<i>Пример</i>  
```.env
POSTGRES_DB=database
POSTGRES_HOST=localhost
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_PORT=5432

DB_CONNECT_RETRY=20
DB_POOL_SIZE=15

APP_HOST=http://127.0.0.1
APP_PORT=8080
PATH_PREFIX=/api/v1

SECRET_KEY=secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080
```

Создание виртуального окружения и установка зависимостей:

- `poetry install`

Активация виртуального окружения:

- `poetry shell`

Развертываение базы данных

- `make db`

Проведение миграций базы данных

- `make migrate`

Запуск сервиса

- `make run`

Далее можно отрыть сайт с докумментацией сервиса и оттуда же отправлять запросы.

Ссылка на документацию сервиса будет иметь вид `APP_HOST:APP_PORT/docs` (APP_HOST, APP_PORT будут браться из файли `.env`).

Ссылка с окружением из примера [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs).

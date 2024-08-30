# [NoteTT](https://github.com/VictorVolkov7/notes_tt)


## Оглавление:

- [Технологии](#технологии)
- [Описание проекта](#Описание-проекта)
- [Права пользователей](#Права-пользователей)
- [Установка и запуск проекта](#установка-и-запуск-проекта)
- [Автор](#Автор)

## Технологии:

- Python 3.12
- Fastapi 0.112.2
- SQLAlchemy 2.0.32
- Alembic 1.13.2
- Uvicorn 0.30.6
- aiohttp 3.10.5
- Яндекс.Спеллер

## Описание проекта:

Python сервис,
предоставляющий REST API интерфейс с методами:
- добавление и вывод списка заметок;
- Регистрация, аутентификация и авторизация пользователей/


## Права пользователей:

### Авторизованный пользователь может:

Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.


## Установка и запуск проекта

### Запуск проекта:

* Клонируйте репозиторий и перейдите в него:
```
git clone https://github.com/VictorVolkov7/notes_tt
```
Создайте и активируйте виртуальное окружение:

```
poetry shell
```

* Установите зависимости из файла requirements.txt и обновите pip:

```
poetry install
```

* Создайте .env файл в корневой папке проекта. В нем должны быть указаны переменные из файла .env.sample.
```
#  postgresql connection sample
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
POSTGRES_USER=postgres_username
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=your_database_name

# auth sample
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```

### Запуск проекта:
Осуществляется с помощью контейнеров Docker:
```
docker compose build

или

docker-compose build
```
Запустить проект:
```
docker compose up -d

или

docker-compose up -d
```
Сервис NoteTT будет доступен по адресу: http://127.0.0.1:8000. Документация к проекту по http://127.0.0.1:8000/docs


## Автор

[Volkov Victor](https://github.com/VictorVolkov7/)
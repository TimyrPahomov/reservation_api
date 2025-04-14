# Reservation_API

Данный проект создан в качестве тестового задания в соответствии с техническим заданием и позволяет бронировать столики в ресторане.

Для пользователей реализованы следующие возможности:
- создание и удаление столика;
- создание и удаление броней;
- просмотр списка столиков и броней;

## Содержание
- [Технологии](https://github.com/TimyrPahomov/reservation_api#технологии)
- [Запуск с помощью Docker](https://github.com/TimyrPahomov/reservation_api#запуск-с-помощью-docker)
- [Доступ к проекту](https://github.com/TimyrPahomov/reservation_api#доступ-к-проекту)
- [Тестирование](https://github.com/TimyrPahomov/reservation_api#тестирование)
- [Автор](https://github.com/TimyrPahomov/reservation_api#автор)

## Технологии
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Docker](https://docs.docker.com/)

## Запуск с помощью Docker

1. Скачать Docker с [официального сайта](<https://www.docker.com/>), установить и запустить его.

2. Клонировать репозиторий и перейти в него:

```sh
git clone https://github.com/TimyrPahomov/reservation_api.git
cd reservation_api/
```

3. Далее нужно осуществить сборку контейнеров:

```sh
docker compose up
```

4. Затем следует собрать статику приложения и выполнить миграции. 
Для этого в новом терминале перейдите в директорию с файлом 'docker-compose.yml' и выполните следующие команды:

```sh
docker compose exec backend python manage.py collectstatic
docker compose exec backend python manage.py migrate
```

## Доступ к проекту
У проекта реализованы следующие эндпоинты:

```sh
http://127.0.0.1:8000/admin/
http://127.0.0.1:8000/api/tables/
http://127.0.0.1:8000/api/tables/<table_id>/
http://127.0.0.1:8000/api/reservations/
http://127.0.0.1:8000/api/reservations/<reservation_id>/
```

## Тестирование
Проект покрыт тестами, для их запуска нужно в директории с файлом 'docker-compose.yml' ввести команду:

```sh
docker compose exec pytest
```

## Автор
[Пахомов Тимур](<https://github.com/TimyrPahomov/>)
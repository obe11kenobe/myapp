# Минимальное веб-приложение для управления сотрудниками

## Описание
Приложение позволяет управлять списком сотрудников: отображать, добавлять, изменять должность и удалять записи. Реализовано с использованием Django 1.11, PostgreSQL (с raw-запросами) и чистого JavaScript (с Bootstrap 5 для стилей).

## Технологии
- Python 3.6.15
- Django 1.11
- PostgreSQL
- Bootstrap 5 (только для стилей)
- JavaScript (без фреймворков)

## Установка
1. Установите Python 3.6 и PostgreSQL.
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте его: `source venv/bin/activate` (на macOS/Linux) или `venv\Scripts\activate` (на Windows)
4. Установите зависимости: `pip install django==1.11 psycopg2-binary`
5. Настройте базу данных в `myapp/settings.py` (имя базы: `my_database`, пользователь: `obekenobe`).
6. Выполните SQL-скрипт: `psql -U obekenobe -d my_database -f create_tables.sql`
7. Запустите сервер: `python manage.py runserver`

## Функционал
- Отображение списка сотрудников (ФИО, пол, возраст, должность, категория).
- Добавление, удаление и изменение должности через интерфейс.
- Обмен данными в формате JSON.

## Автор
Обе Кенобе (obekenobe)

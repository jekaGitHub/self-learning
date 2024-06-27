# self-learning
Проект самообучения. 
Платформа работает только с авторизованными пользователями. 
Платформа содержит функционал разделов и материалов. После изучения материалов можно пройти тестирование.

Технологии:

- python 3.11
- postgresql
- os
- dotenv

Используемые библиотеки:

- Django
- pillow
- psycopg2-binary
- python-dotenv

Инструкция по развертыванию проекта:

1. Клонировать проект:
  https://github.com/jekaGitHub/self-learning.git

2. Создать виртуальное окружение:
  В терминале запустить команды:

    python -m venv venv
    source venv/bin/activate

3. Установить зависимости:
  Для установки всех зависимостей в терминале необходимо запустить команду:

    pip install -r requirements.txt

4. Cоздать базу данных:
  В терминале введите команду:

    CREATE DATABASE database_name

5. Применить миграции:
  В терминале введите команды:

    python3 manage.py makemigrations 
    python3 manage.py migrate

6. Заполнить файл .env по образцу .env.sample
7. Для создания суперпользователя необходимо применить команду:
    python3 manage.py csu
8. Для запуска проекта использовать команду: 
    python manage.py runserver

Автор проекта: Евгений Сафонов

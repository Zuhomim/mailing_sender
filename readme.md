# Mailing Sender
## Установка:
```
**1) https://github.com/Zuhomim/mailing_sender
2) "Fork" repository
3) git clone созданного репозитория в Вашем Git-аккаунте**
```

### Установка зависимостей:
```
**pip install -r requirements.txt**
```

### Создание Суперпользователя:
```
**python manage.py csu**
```

### Шаблон файла .env с переменными - **.env.template**

### Запуск сервера:
```
python manage.py runserver
```

## Структура:
### Раздел blog
#### - приложение с шаблоном лендинговой страницы блоговых записей

### Раздел config
#### - settings.py - основной конфигурационный файл
#### - urls.py - файл ссылочной целостности всего django-проекта

### Раздел mailing
#### - сервис рассылки сообщений (message) создаваемым клиентам (clients)
#### - содержит команду runapscheduler для запуска (каждые 30 сек) функции my_job в файле service.py

### Раздел media
#### - служит для сохранения media-файлов

### Раздел static
#### - css, js шаблоны библиотеки Bootstrap

### Раздел users
#### - приложение с моделью пользователей
#### - настраиваются в том числе в админке (http://127.0.0.1:8000/admin) с помощью данных суперпользователя
#### (users/management/commands/csu)
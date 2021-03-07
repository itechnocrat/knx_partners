## Изучение Django
[Учебник Django: Веб-сайт местной библиотеки](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Tutorial_local_library_website)  
[Руководство по Django часть 2: создание скелета](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/skeleton_website)  
```sh
django-admin startproject locallibrary .
cd locallibrary
```
`startproject` created:  
```sh
some_external_directory/
    manage.py
    locallibrary/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
`startproject` создает общий каркас всех будущих приложений, в противоположность `startapp`, которая создает каркасы внутренних приложений.  
`settings.py` содержит в себе все настройки проекта.  
Здесь мы регистрируем приложения, задаём размещение статичных файлов, настройки базы данных и так далее.  
`urls.py` задаёт ассоциации url адресов с представлениями.  
Несмотря на то, что этот файл может содержать все настройки url, обычно его делят на части, по одной на приложение, как будет показано далее.  
`wsgi.py` используется для налаживания связи между вашим Django приложением и веб-сервером.  
Вы можете воспринимать его, как утилиту.  
`manage.py` используется для создания приложений, работы с базами данных и для запуска отладочного сервера.  

Находясь на уровне `manage.py`:  
```sh
python manage.py startapp catalog
```
Будет создан:  
каталог `catalog` с содержимым:  
`migrations` хранит "миграции" — файлы, которые позволяют автоматически обновлять базу данных по мере изменения моделей, 
`__init__.py` — пустой файл для того, чтобы Django и Python распознавали папку как Python модуль и позволяет нам использовать его объекты внутри других частей проекта,  
настройки административной части - в admin.py,  
регистрация приложения - в apps.py, уже содержат некоторый шаблонный код для работы с вышеназванными объектами,  
модели - в models.py,  
тесты - в tests.py, 
контроллеры (views) должны находится - в views.py.  

После создания приложения, его нужно зарегистрировать в проекте.  
Приложения регистрируются добавлением их названий в список INSTALLED_APPS в `settings.py`:  
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog.apps.CatalogConfig', # добавлено для регистрации
]
```
Это указание на класс `CatalogConfig`, в `catalog/apps.py`.  
В этом же файле сделать `TIME_ZONE = 'Europe/Moscow'`  
`SECRET_KEY` - секретный ключ, который используется Django для поддержки безопасности сайта.  
При компрометации - сменить.  
`DEBUG` - подробные сообщения об ошибках, вместо стандартных HTTP статусов ответов.  
`False` для продакшена.  

### Подключение URL-адреса

`django-admin startproject locallibrary` создал файл `locallibrary/urls.py`, похоже, что это роутер, этот роутер можно использовать для обработки всех входящих URLs, но лучше создавать совй роутер для каждого приложения.  

Задрал перевод-калька с английского на русский-птичий, бросил, перехожу на оф. мануал - ветка pool (по названию учебного приложения).

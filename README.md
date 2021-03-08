## Изучение Django
[Django documentation](https://docs.djangoproject.com/en/3.1/)  
[Getting started](https://docs.djangoproject.com/en/3.1/intro/)  
### Запуск окружения разработки
В к.л. директорию сделать клон этого репозитория:  
```sh
gh repo clone itechnocrat/knx_partners
```
or  
```sh
git clone https://github.com/itechnocrat/knx_partners
```
Перейти в каталог:  
```sh
cd knx_partners
```
В терминале/консоли OS:  
переключиться на ветку `poll`:  
```sh
git checkout poll
```
запустить MS VS Code:  
```sh
code .
```
В MS VS Code установить плагин [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):  
Launch VS Code Quick Open `Ctrl+P`, paste `ext install ms-vscode-remote.remote-containers` command, and press enter.  

Как только плагин установится, MS VS Code, в правом нижнем углу, выбросит сообщение с предложением перезапустить текущий каталог в контейнере.  
Согласиться.  
Если не выбросит, то "встряхнуть" - просто перезапустить MS VS Code.  
Есть и другие способы запустить сборку контейнера - https://code.visualstudio.com/docs/remote/containers-tutorial  
MS VS Code перезапустится и начнется сборка контейнера.  
Дождаться окончания процесса.  
Запустить терминал MS VS Code, в терминале должно быть красивое приглашение командной строки.  
### Writing your first Django app
### Poll application
consist of two parts:  
1.
A public site that lets people view polls and vote in them.  
2.
An admin site that lets you add, change, and delete polls. 
### [Part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)  
### Creating a project
```sh
python -m django --version # Пнуть Django
django-admin startproject capsule . # генерация минимальной структуры приложения
cd capsule
```
`startproject` created:  
```sh
../
    manage.py
    capsule/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
 - `manage.py` - A command -line utility that lets you interact with this Django project in various ways.  
 - `capsule/` - directory is the actual Python package for your project.  
Its name is the Python package name you’ll need to use to import anything inside it (e.g. capsule.urls).  
 - `capsule/__init__.py` - An empty file that tells Python that this directory should be considered a Python package.  
 - `capsule/settings.py` - Settings/configuration for this Django project.  
 - `capsule/urls.py` - The URL declarations for this Django project; a “table of contents” of your Django -powered site.  
 - `capsule/asgi.py` - An entry -point for ASGI -compatible web servers to serve your project.  
See [How to deploy with ASGI](https -//docs.djangoproject.com/en/3.1/howto/deployment/asgi/) for more details.
 - `capsule/wsgi.py` - An entry -point for WSGI -compatible web servers to serve your project.  
See [How to deploy with WSGI](https -//docs.djangoproject.com/en/3.1/howto/deployment/wsgi/) for more details. 
### Пробный запуск
В терминале MS VS Code ввести:  
```sh
python manage.py runserver
```
Полюбоваться и остановить сервер `Ctrl+C`  
### Создание основного приложения

Находясь в том же каталоге, что и `manage.py`:  
```sh
python manage.py startapp polls
```
=>  
```sh
../
    polls/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
```
### Write your first view
```py
# polls/views.py¶

from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
Чтобы Django мог послать такой ответ, нужно связать `views.py` (функцию `index()`) с каким-то URL, для этого нужен, т.н. `URLconf` приложения:  
```sh
touch polls/urls.py
```
```py
# polls/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```
Это еще не все, `URLconf` всего приложения, это `capsule/urls.py`, ничего не знает об `URLconf` приложения, это `polls/urls.py`.  
Необходимо это изменить:  
```py
# capsule/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path() передает все, что после polls/ в include()
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```
Проверим сваренное:  
запустим сервер:
```sh
python manage.py runserver
```
и перейдем по адресу [http://localhost:8000/polls/](http://localhost:8000/polls/)  
Полюбоваться и остановить сервер `Ctrl+C`  

Функции `path()` передается четыре аргумента, два первых обязательны, два других - нет.  
1.
Первый, это шаблон запроса,  
2. 
второй - вызов представления.  
В процессе выполнения запроса, Django просматривает `urlpatterns` сверху вниз в поиске совпадения шаблона с последоменной частью запроса и до параметров `POST`/`GET`.  
Как только будет найдено совпадение, произойдет вызов функции представления (второй арг. `path()`), с первым аргументом - объектом `HttpRequest`, где похоже будут и параметры `POST`/`GET`, но это не точно.  
3. Аргументы параметров `POST`/`GET`, но это не точно.  
4. Имя для URL.  

### [Part 2](https://docs.djangoproject.com/en/3.1/intro/tutorial02/)  
#### Database setup
Посмотрим файл всех настроек Django:  
```py
# capsule/settings.py

TIME_ZONE = 'Europe/Moscow'
# предустановленные Django приложения
INSTALLED_APPS = [
    'django.contrib.admin', # The admin site. You’ll use it shortly.
    'django.contrib.auth', # An authentication system.
    'django.contrib.contenttypes', # A framework for content types.
    'django.contrib.sessions', # A session framework.
    'django.contrib.messages', # A messaging framework.
    'django.contrib.staticfiles', # A framework for managing static files.
]
```
Подготовить БД (встроенная поддержка):  
```sh
python manage.py migrate
```
Команда создает БД и таблицы в ней в соответствии с настройками из файла `polls/settings.py`  
### Creating models
Модель в понимании термина MVT - Model, View, Template.  
Модель, это ...

Приложение будет содержать две модели:  
Question and Choice (вопрос и выбор).  
У модели Question есть вопрос и дата публикации. 
У модели Choice есть два поля: текст выбора и подсчет голосов, выбор связан с вопросом.  
Модели описываются классами Pyhton.  
Edit the polls/models.py file so it looks like this:  
```py
# polls/models.py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```
Каждый класс является подклассом `django.db.models.Model`.  
Each model has a number of class variables, each of which represents a database field in the model.  
Каждая модель имеет ряд переменных класса, каждая из которых представляет поле базы данных в модели.  
... ToDo сформулировать точности

### Activating models
Небольшое кол-во кода дает Django много информации для создания схемы базы данных приложениия и создания API для доступа к объектам Question and Choice.  

Нужно сообщить проекту, что приложение Poll существует.  
(Приложения Dj устанавливаемые, их можно исп-ть во множестве проектов.)  
Для регистрации приложения необходимо добавить его класс конфигурации `PollsConfig` из файла `polls/apps.py` в `INSTALLED_APPS` файла `mysite/settings.py`:  
```py
# capsule/settings.py

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    # ...
]
```
Теперь Dj знает о приложении и как его подключить.  
Необходимо сообщить Dj об изменениях в моделях данных, они будут сохранены в миграциях, это файлы в `polls/migrations/*_initial.py`  
```sh
python manage.py makemigrations polls
```
Миграции можно посмотреть в виде SQL запросов:  
```sh
python manage.py sqlmigrate polls 0001
```
Теперь необходимо создать модель таблиц в реальной БД:  
```sh
python manage.py migrate
```
Итого, как вносятся изменения в модель данных:  
Изменяется `polls/models.py` и  
```sh
python manage.py makemigrations
python manage.py migrate
```
### [Playing with the API](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api)
```sh
python manage.py shell
quit()
```

### Creating an admin user
First we’ll need to create a user who can login to the admin site. Run the following command:  
```sh
python manage.py createsuperuser
# Username: technocrat
# Email address:
# Password: technocrat
python manage.py runserver
```
[http://localhost:8000/admin/](http://localhost:8000/admin/)  
Залогиниться под админом.  
### Make the poll app modifiable in the admin
```py
# polls/admin.py¶

from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
Обновить страницу в браузере, изменения станут сразу же заметны.  
Таблица Question стала доступной для редактирования в административной части сайта.  
### [Explore the free admin functionality](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#explore-the-free-admin-functionality)  

---
Старое  
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

`django-admin startproject capsule` создал файл `capsule/urls.py`, похоже, что это роутер, этот роутер можно использовать для обработки всех входящих URLs, но лучше создавать совй роутер для каждого приложения.  

Задрал перевод-калька с английского на русский-птичий, бросил, перехожу на оф. мануал - ветка pool (по названию учебного приложения).

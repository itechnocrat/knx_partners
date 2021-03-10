# Изучай Django во имя добра
## Изучение Django на примере приложения Poll
[Django documentation](https://docs.djangoproject.com/en/3.1/)  
[Getting started](https://docs.djangoproject.com/en/3.1/intro/)  
### Создание и запуск окружения разработки
Сделать клон этого репозитория в любую директорию:  
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
# предустановленные Django-приложения
INSTALLED_APPS = [
    'django.contrib.admin', # The admin site. You’ll use it shortly.
    'django.contrib.auth', # An authentication system.
    'django.contrib.contenttypes', # A framework for content types.
    'django.contrib.sessions', # A session framework.
    'django.contrib.messages', # A messaging framework.
    'django.contrib.staticfiles', # A framework for managing static files.
]
```
Подготовить БД (встроенная поддержка SQLite):  
```sh
python manage.py migrate
```
Команда создает БД с таблицами в соответствии с настройками БД из файла `capsule/settings.py` и миграциями, поставляемыми с приложением(ми) (об этом дальше).
Каждая выполненная миграция отображается сообщением о выполнении в терминале.  
Приложения, перечисленные в `INSTALLED_APPS` в файле `capsule/settings.py` нужны не всем и не всегда, некоторые можно отключить, `migrate` будет выполнять миграции только для указанных приложений.  
### Creating models
Модель в понимании термина MVT - Model, View, Template.  
Модель, это макет БД с метаданными.  

Philosophy:  
Модель содержит осн. поля и поведение данных.  
Цель - в определении модели данных в одном месте и извлечении из нее данных.  
Миграции основаны на файлах моделей.  

Приложение будет содержать две модели:  
Question and Choice (вопрос и выбор).  
У модели Question есть содержание вопроса и дата публикации.  
У модели Choice есть два поля: текст выбора и количество голосов.  
Выбор связан с вопросом.  
Модели описываются классами Python.  
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
Модели представляется классом - подклассом `django.db.models.Model`.  
Each model has a number of class variables, each of which represents a database field in the model.  
Модель имеет переменные которые представляют поля таблиц базы данных.  
Поля, это экземпляры класса `Field`.  

> The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.

>You can use an optional first positional argument to a Field to designate a human-readable name. That’s used in a couple of introspective parts of Django, and it doubles as documentation. If this field isn’t provided, Django will use the machine-readable name. In this example, we’ve only defined a human-readable name for Question.pub_date. For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.

>Some Field classes have required arguments. CharField, for example, requires that you give it a max_length. That’s used not only in the database schema, but in validation, as we’ll soon see.

>A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

>Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
### Activating models
Небольшое кол-во кода дает Django много информации для создания схемы базы данных приложения и создания API для доступа к объектам Question and Choice.  

Нужно сообщить проекту, что приложение Poll существует.  
(Приложения Dj устанавливаемые, их можно исп-ть во множестве проектов.)  
Для регистрации приложения необходимо добавить его класс конфигурации - `PollsConfig()` из файла `polls/apps.py`, в `INSTALLED_APPS` файла `capsule/settings.py`:  
```py
# capsule/settings.py

INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    # ...
]
```
Теперь Dj знает о приложении и о том, как его подключить.  
Необходимо сообщить Dj об изменениях в моделях данных, они будут сохранены в миграциях, это файлы в `polls/migrations/*_initial.py`:  
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
python manage.py makemigrations polls
python manage.py migrate
```
### [Playing with the API](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#playing-with-the-api)
```sh
python manage.py shell
# смысл пока ускользнул
quit()
```

### Creating an admin user
First we’ll need to create a user who can login to the admin site.  
Run the following command:  
```sh
python manage.py createsuperuser
# Username: technocrat
# Email address:
# Password: technocrat
python manage.py runserver
```
Перейти по адресу [http://localhost:8000/admin/](http://localhost:8000/admin/) и
залогиниться под админом.  
### Make the poll app modifiable in the admin
```py
# polls/admin.py¶

from django.contrib import admin

from .models import Question

admin.site.register(Question)
```
Обновить страницу в браузере, результаты станут сразу же заметны.  
Таблица Question стала доступной для редактирования в административной части сайта.  
[Explore the free admin functionality](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#explore-the-free-admin-functionality)  

### [Part 3](https://docs.djangoproject.com/en/3.1/intro/tutorial03/)  
### Writing more views
Добавим представление, которое будет способно принимать аргументы: 
```py
# polls/views.py¶

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```
Теперь необходимо подключить новое представление к приложению/модулю polls:  
```py
# polls/urls.py¶

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
```
При поступлении запроса `http://localhost:8000/polls/34/`, Dj загружает модуль `capsule/urls`, т.к. он указан в переменной `ROOT_URLCONF` файла `capsule/settings.py`, просматривает по порядку список из переменной `urlpatterns` в `capsule/urls`, находит совпадение `polls/`, вызывает `polls.urls`, которому передается `34/`, что совпадает с шаблоном `<int:question_id>/`, из-за чего вызывается `detail()` из файла `polls/views.py`.  
Угловые скобки «захватывают» часть URL-адреса и передают ее как аргумент ключевого слова в представление, `detail()` получает аргументы `request=<HttpRequest object>` и `question_id=34`  
`question_id`, это имя, которое будет использоваться для идентификации совпадающего шаблона.  
### Write views that actually do something
Представления ответственны за две вещи:  
- возвращают `HttpResponse` объект, содержащий контент  
- возвращает [Http404](https://docs.djangoproject.com/en/3.1/topics/http/views/#django.http.Http404)  

Представления читают записи из БД (собственно представляют/отображают их), используя для этого систему шаблонизирования, как в Dj - `DjangoTemplates` или другие.  
Могут быть сгенерированы файлы: PDF, XML, ZIP на лету, все, что хотите, используя библиотеки Python.  
```py
# polls/views.py¶

from django.http import HttpResponse

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

# Leave the rest of the views (detail, results, vote) unchanged
```
Смысл пока не понятен.  
Плавно подходим к системе шаблонов в Dj.  
Система шаблонов отделяет дизайн страниц от Python.  
Создание структуры каталогов шаблонов и шаблона `templates` для хранения шаблонов:  
```sh
mkdir -p polls/templates/polls
touch polls/templates/polls/index.html
```
В переменной `TEMPLATES` в файле `capsule/settings.py` описывается, как Django будет загружать и обрабатывать шаблоны.  
`DjangoTemplates` включается по умолчанию значением `true` переменной `APP_DIRS` в файле `capsule/settings.py`  
`DjangoTemplates` всегда ищет подкаталог `templates` в каждом из `INSTALLED_APPS`.  
Загрузчик шаблонов `app_directories` позволяет обращаться к шаблонам коротко - `polls/index.html`.  

Тёмная тема про `Template namespacing` ...
Наполним шаблон содержимым:  
```html
<!-- polls/templates/polls/index.html¶ -->
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
Обновим  `polls/views.py`:  
```py
# polls/views.py¶

from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
Внутри функции загружается шаблон и ему передается контекст - соответствие имен переменных в шаблоне объектам Python.  
Полюбуемся:  
```sh
python manage.py runserver
```
Если был утрачен файл базы данных то понадобится повторить действия из Part 2:  
```sh
python manage.py makemigrations #?
python manage.py migrate
python manage.py createsuperuser
# Username: technocrat
# Email address:
# Password: technocrat
```
Залогиниться [http://localhost:8000/admin/](http://localhost:8000/admin/) и создать вопрос, и тогда [http://127.0.0.1:8000/polls/](http://127.0.0.1:8000/polls/) отобразит маркированный список вопросов.  

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

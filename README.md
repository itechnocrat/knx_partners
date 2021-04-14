# KNX.Partners

## Разработка

Делать будем с помощью:

[Django](https://www.djangoproject.com/)

[Django documentation](https://docs.djangoproject.com/en/3.2/)

[Bootstrap](https://getbootstrap.com/)

[django-bootstrap5](https://django-bootstrap5.readthedocs.io/en/latest/index.html)

[django-bootstrap5](https://pypi.org/project/django-bootstrap5/)

Модель данных см. в `proto.uxf`, для просмотра необходим плагин для VS Code - [UMLet](https://marketplace.visualstudio.com/items?itemName=TheUMLetTeam.umlet).  

## Part 1: Start

Пропускаем из-за большого кол-ва воды.
## Part 2: Creating a skeleton website

1. Use the `django-admin` tool to generate a project folder, the basic file templates, and `manage.py`.  
2. Use `manage.py` to create one or more applications.  
Note: A website may consist of one or more sections. For example, main site, blog, wiki, downloads area, etc.  
3. Register the new applications to include them in the project.  
4. Hook up the url/path mapper for each application.  

```sh
knx_partners/         # Website folder
    manage.py         # Script to run Django tools for this project (created using django-admin)
    knx_partners/     # Website/project folder (created using django-admin)
    catalog/          # Application folder (created using manage.py)
```

### Creating the project

```sh
django-admin startproject knx_partners
```

=>  

```sh
knx_partners/         # Website folder
    prob/             # Application folder (created using manage.py)
    knx_partners/     # Website/project folder (created using django-admin)
        __init__.py
        settings.py
        urls.py
        wsgi.py
        asgi.py
    manage.py         # Script to run Django tools for this project (created using django-admin)
```

### Creating the catalog application

```sh
cd knx_partners
python manage.py startapp prob
```

### Registering the catalog application

Приложение должно быть зарегистрировано для того, чтобы оно было учтено при запуске любых инструментов, например, добавление моделей в БД.  

Приложения регистрируются в списке `INSTALLED_APPS` файла `knx_partners/knx_partners/settings.py`  

```py
INSTALLED_APPS += [
    'catalog.apps.CatalogConfig', #This object was created for us in /catalog/apps.py
    'django_bootstrap5',
]
```

### Specifying the database

`DATABASES` файл `knx_partners/knx_partners/settings.py`  

### Other project settings

`TIME_ZONE = 'Europe/Moscow'` файл `knx_partners/knx_partners/settings.py`  

### Hooking up the URL mapper

[URL dispatcher](https://docs.djangoproject.com/en/3.1/topics/http/urls/)  

```py
# knx_partners/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('prob/', include('prob.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='prob/', permanent=True)),
]

# обслуживание статических файлов во время разработки
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

```sh
touch prob/urls.py
```

```py
# prob/urls.py

from django.urls import path
from . import views

urlpatterns = [

]
```

### Testing the website framework

```py
cd knx_partners
python manage.py makemigrations
python manage.py migrate
```

Эти команды необходимо повторять каждый раз, когда изменяются модели.  

### Running the website

```sh
python manage.py createsuperuser
# admin
# admin@poka.net
# admin
python manage.py runserver
```

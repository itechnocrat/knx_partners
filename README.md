# KNX.Partners

## Разработка

### Попробуем что-то создать

думать будем с помощью этого: https://docs.djangoproject.com/en/3.1/topics/forms/

В миниатюре надо сделать простую html-форму, ее отправку, сохранение данных формы, далее посмотрим.

В UML нарисуем модель DB

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
    catalog/          # Application folder (created using manage.py)
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

### Specifying the database

`DATABASES` файл `knx_partners/knx_partners/settings.py`  

### Other project settings

`TIME_ZONE = 'Europe/Moscow'` файл `knx_partners/knx_partners/settings.py`  

### Hooking up the URL mapper

```py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

```sh
cd ../catalog
touch ./urls.py
```

```py
from django.urls import path
from . import views

urlpatterns = [

]
```

### Testing the website framework

```py
cd ..
python manage.py makemigrations
python manage.py migrate
```

Эти команды необходимо повторять каждый раз, когда изменяются модели.  

### Running the website

```sh
python manage.py runserver
```

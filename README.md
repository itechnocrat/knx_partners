## KNX.Partners
Описание проекта пока отсутствует.
### Описание репозитория
Изначально содержит две ветки:  
`master`  
и  
`demo`  

`master` содержит конфигурацию Docker-контейнера под плагин для MS VS Code - `Remote - Containers`.  
О технологии [здесь](https://code.visualstudio.com/docs/remote/remote-overview)  
Созданный по этой конфигурации контейнер будет содержать в себе только Python, Django и PostgreSQL-сервер, плюс др. инструменты, с помощью которых можно начать создавать приложение.  
PostgreSQL-сервер пока не трогаем, он просто есть, что уже хорошо.  

`demo` дополнительно к выше упомянутой конфигурации, содержит учебный код небольшого приложения `Django Tutorial in Visual Studio Code`, работу которого можно реально увидеть в веб-браузере.  
### Запуск "Django Tutorial in Visual Studio Code"
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
переключиться на ветку `demo`:  
```sh
git checkout demo
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
Запустить терминал MS VS Code, в терминале должно быть красивое приглашение командной строки и  
отдать команды:  
```sh
python manage.py migrate # создаст файл базы данных SQLite
python manage.py runserver # запустит встроенный в Python веб-сервер
```
Запустится веб-сервер, встроенный в Python, а MS VS Code, в правом нижнем углу, предложит пробросить порт из контейнера наружу.  
Согласиться.  
Теперь можно поиграться (см. мануал `Django Tutorial in Visual Studio Code` далее).  
На этом ознакомление со окружением разработки и Django можно считать законченной.  
Следует закрыть терминал MS VS Code, отсоединиться от контейнера.  
### Начало разработки
Переключиться на ветку `master` или `develop` / `feature` и начать погружение, вооружившись документацией:   
[Writing your first Django app, part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)  
[MDN. Django введение](https://developer.mozilla.org/ru/docs/Learn/Server-side/Django/Introduction)  
[Django Software Foundation](https://www.djangoproject.com/)  

__Всегда внимательно следи за текущей веткой!!!__

### Основа реализации
[Django Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-django)  
Из [репозитория](https://github.com/microsoft/python-sample-vscode-django-tutorial) взято:  
`python-sample-vscode-django-tutorial/.vscode/launch.json` и подредактирован.  
`python-sample-vscode-django-tutorial/hello/`  
`python-sample-vscode-django-tutorial/python-sample-vscode-django-tutorial/manage.py`  
`python-sample-vscode-django-tutorial/requirements.txt` и подредактирован.  
`python-sample-vscode-django-tutorial/uwsgi.ini`  
`python-sample-vscode-django-tutorial/web_project/`  
и  
[VS Code Remote / GitHub Codespaces Container Definitions](https://github.com/microsoft/vscode-dev-containers)  
Использована готовая конфигурация -  
`vscode-dev-containers/containers/python-3-postgres`  
из которой взят только `.devcontainer` и в нем подредактированы файлы конфигурации.  
### .devcontainer
В файле `.devcontainer/devcontainer.json` прописаны дополнительные плагины, которые будут доступны MS VS Code после подключения к контейнеру.  
Это позволяет один раз настроить среду разработки и потом много раз пользоваться, а так же, обмениваться ей с другими разработчиками.  

# KNX.Partners

## Описание проекта

пока отсутствует

### Описание ветки master

`master` содержит конфигурацию Docker-контейнера под плагин для MS VS Code - [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).  
О технологии [здесь](https://code.visualstudio.com/docs/remote/remote-overview)  
Созданный по этой конфигурации контейнер будет содержать в себе только Python, Django и PostgreSQL-сервер, плюс др. инструменты, с помощью которых можно начать создавать приложение.  
PostgreSQL-сервер пока не трогаем, он просто есть.  
  
### Запуск "Django Tutorial in Visual Studio Code"

В любую директорию сделать клон этого репозитория:  

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

запустить MS VS Code:  

```sh
code .
```

В MS VS Code установить плагин [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):  
Launch VS Code Quick Open `Ctrl+P`, paste `ext install ms-vscode-remote.remote-containers` command, and press enter.  

Как только плагин установится, MS VS Code, в правом нижнем углу, выбросит сообщение с предложением перезапустить текущий каталог в контейнере.  
Согласиться.  
Если не выбросит, то "встряхнуть" - просто перезапустить MS VS Code.  
Есть и другие способы запустить сборку контейнера - <https://code.visualstudio.com/docs/remote/containers-tutorial>  
MS VS Code перезапустится и начнется сборка контейнера.  
Дождаться окончания процесса.  
Запустить терминал MS VS Code, в терминале должно быть красивое приглашение командной строки.  
Возможно увидеть версию Python и Django:  

```sh
python --version
# python -c "import django; print(django.get_version())"
python -m django --version
```

На этом ознакомление со окружением разработки и Django можно считать законченной.  
Следует закрыть терминал MS VS Code, отсоединиться от контейнера.  

### Начало разработки с Django

Переключиться на какую-то ветку и начать:
[Django documentation](https://docs.djangoproject.com/en/3.1/)  
[MDN Web Docs, moz://a: Веб-фреймворк Django (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)  

### Основано на

[VS Code Remote / GitHub Codespaces Container Definitions](https://github.com/microsoft/vscode-dev-containers)  
Использована готовая конфигурация -  
`vscode-dev-containers/containers/python-3-postgres`  
из которой взят только `.devcontainer` и в нем подредактированы файлы конфигурации.  

### .devcontainer

В файле `.devcontainer/devcontainer.json` прописаны дополнительные плагины, которые будут доступны MS VS Code после подключения к контейнеру.  
Это позволяет один раз настроить среду разработки и потом много раз пользоваться, а так же, обмениваться ей с другими разработчиками.  

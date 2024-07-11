# Virtual-Machine-API

To set up requirements run *pip install -r requirements.txt*

# Mail server

- Создать файл `.env` на основе файла `.env.dist` в папке mail_server и изменить в нем соответствующие переменные. [Wiki](https://github.com/jeboehm/docker-mailserver/wiki/Configuration-variables) на английском.
- Выполнить команду `mail_server/bin/production.sh pull` для загрузки нужных образов.
- Выполнить команду `mail_server/bin/production.sh up -d` для запуска сервисов.
- Создать первый адрес электронной почты и имя пользователя с правами администратора командой `mail_server/bin/production.sh run --rm web setup.sh`. Мастер установки задаст несколько вопросов, чтобы все настроить.

Подробнее можно прочитать на [GitHub](https://github.com/jeboehm/docker-mailserver)
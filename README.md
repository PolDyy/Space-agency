# Space-agency

## Запуск с помощью docker-compose

1) Создаем директорию для проекта и переходим в него  

2) Клонируем репозиторий с github:  

    `git init`  

    `git clone https://github.com/PolDyy/Space-agency.gi)`

3) Создаем файл .env на основе env_example

4)  Проверяем установлен ли докер, если нет, то устанавливаем его  
(обратитесь к документации Docker)

5) Перейти в корневую папку проекта (на уровне с docker-compose.yml).

6) Использовать команду.

  `docker compose up -d --build`

7) Создать супер пользователя:

  `docker exec agency bash entrypoint.sh`

### Обратите внимание 

Логин и пароль для входа в админ-панель создаются автоматически на базе переменных окружения: DJANGO_SUPERUSER_USERNAME и DJANGO_SUPERUSER_PASSWORD  

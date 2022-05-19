# Сайт доставки еды Star Burger

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.

## Как запустить dev-версию сайта

Для запуска сайта нужно запустить **одновременно** бэкенд и фронтенд, в двух терминалах.

### Как собрать бэкенд

- Скачайте код:
```sh
https://github.com/Yulia51188/star-burger-d
```

- Перейдите в каталог проекта:
```sh
cd star-burger-d
```

- [Установите Docker](https://docs.docker.com/engine/install/), если этого ещё не сделали.

Проверьте, что `docker` и `docker-compose` установлены и корректно настроены. Выполните в командной строке:
```sh
$ docker --version
Docker version 20.10.14, build a224086
$ docker compose version
docker-compose version 1.27.4, build 40524192
```

- Соберите Docker образы с помощью команды:
```sh
docker compose build
```

- Контейнеры будут использовать монтированные внешние папки для медиа-файлов и файлов верстки. Пропишите свои пути в файле `docker-compose.yaml`  вместо `./bundles` и `./media` или создайте в текущей директории папки `bundles` и `media`.

```sh
  frontend:
    ...

    volumes:
      - ./bundles:/frontend/bundles
    ...

  backend:
    ...

    volumes:
      - ./bundles:/backend/bundles
      - ./media:/backend/media
    ...
```

- Создайте файл с переменными окружения в каталоге проекта

  - `GEOCODER_TOKEN` - токен для [геокодера Яндекс](https://developer.tech.yandex.ru/services/), чтобы определять расстояние от ресторана до адреса. Обязательная переменная окружения.
  - `ROLLBAR_TOKEN` - токен для сервиса [Rollbar](https://rollbar.com/), чтобы получать сообщения об ошибках, исключая HTTP404. Обязательная переменная окружения.
  - `DATABASE_URL` - конфигурация БД, указывается в виде URL, см. [примеры](https://github.com/jacobian/dj-database-url#id7). Если значение не указано, то используется движок `SQLite`, имя файла `db.sqlite`. Для использования `PostgreSQL` в `requirements.txt` добавлена библиотека [psycorg2](https://pypi.org/project/psycopg2/).
  - `POSTGRES_USER`, `POSTGRES_PASSWORD` - имя пользователя и пароль для авторизации в БД.
  - `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте.

- Запустите контейнеры для фронтенда, базы данных и бэкэнда:

```sh
docker compose up -d
```

- Сделайте первоначальные настройки базы данных и загрузите в нее тестовые данные, если необходимо:

```sh
docker exec -it burger_django python manage.py migrate
docker exec -it burger_django python manage.py createsuperuser
docker exec -it burger_django python manage.py load_initial_data
```

- Откройте сайт в браузере по адресу [http://0.0.0.0:8000/](http://0.0.0.0:8000/) и увидите главную страницу сайта:


- Чтобы увидеть позиции меню, заполните в админке доступные блюда для ресторанов.


## Как запустить prod-версию сайта

### Первоначальное развертывание сайта

- Установите на сервере:
    - [Git](https://github.com/git-guides/install-git)
    - [Docker и Docker Compose](https://docs.docker.com/engine/install/)
    - Настройте [проброс ssh ключа](https://docs.github.com/en/developers/overview/using-ssh-agent-forwarding) для взаимодействия с GitHub при обновлении кода  в репозитории

- Склонируйте проект на свой сервер

```sh
cd /opt/
git clone git@github.com:Yulia51188/star-burger-d.git
git pull
```

- Соберите докер образы фронтенда, бэкэнда и базы данных для продакш-версии

```sh
cd /opt/star-burger-d/production/
docker compose build

```

- Создать файл `.env` в каталоге `./production/` со следующими настройками:

- `DEBUG` — флаг режима отладки. Поставьте `False` для боевого сервера. Если не указан, то True.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте. Не стоит использовать значение по-умолчанию, **замените на своё**.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `GEOCODER_TOKEN` - токен для [геокодера Яндекс](https://developer.tech.yandex.ru/services/), чтобы определять расстояние от ресторана до адреса. Обязательная переменная окружения.
- `ROLLBAR_TOKEN` - токен для сервиса [Rollbar](https://rollbar.com/), чтобы получать сообщения об ошибках, исключая HTTP404. Обязательная переменная окружения.
- `ROLLBAR_ENV_LABEL` - строка, описывающая окружение запущенного проекта, по умолчанию `development`.
- `DATABASE_URL` - конфигурация БД, указывается в виде URL, см. [примеры](https://github.com/jacobian/dj-database-url#id7). Если значение не указано, то используется движок `SQLite`, имя файла `db.sqlite`. Для использования `PostgreSQL` в `requirements.txt` добавлена библиотека [psycorg2](https://pypi.org/project/psycopg2/).
- `POSTGRES_USER`, `POSTGRES_PASSWORD` - имя пользователя и пароль для авторизации в БД.

- Запустить контейнеры

```
docker compose up -d
```

- Скопируйте файлы статики в общую папку

```sh
mkdir static
docker cp burger_django:/backend/staticfiles/. ../static/
docker cp burger_parcel:/frontend/bundles/. ../static/
```

- Примените к базе данных миграции и создайте аккаунт администратора

```sh
docker exec -it burger_django python manage.py migrate
docker exec -it burger_django python manage.py createsuperuser
```

- Соберите образ контейнера с nginx

```sh
docker build -t burger-server ./nginx/
````

- Запустите контейнер nginx с необходимыми настройками
```sh
docker run -d -p 80:80 --network production_nginx_network -v /opt/star-burger-d/media:/media -v /opt/star-burger-d/static --name burger_nginx burger-server
```

- Для обечения бесперебойной работы сайта настройте автоматический перезапуск, выпуск сертификата, очистку устаревших сессий и др.


### Обновление кода

При обновлении кода запустите скрипт для пересборки и перезапуска контейнеров сайта

- в первый раз настройте права на запуск файла

```sh
chmod +x deploy.sh
```
- запустите скрипт, находясь в директории `production`
```sh

./deploy.sh
````

## Информация для проверяющего

- домен [yulyas-burgers.tk](https://docker-burgers.tk/)
- IP [77.223.96.144](https://80.249.149.214/)
- имя пользователя - `root`
- порт ssh, стандартный - `22`
- скрипт для деплоя `/opt/star-burger-d/production/deploy.sh`


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).

Где используется репозиторий:

- Второй и третий урок [учебного модуля Django](https://dvmn.org/modules/django/)

# Проект QRKot
## _Приложение для Благотворительного фонда поддержки котиков_

----
### <anchor>Описание</anchor>
"QRKot" – это инновационное приложение для благотворительного фонда, созданное с целью поддержки нуждающихся котиков.
Фонд организует и ведет различные проекты для сбора пожертвований.<br>
**Проекты**<br>
В рамках фонда может быть запущено несколько проектов. Каждый из них имеет свое название, описание и целевую сумму сбора. Как только проект достигает своей цели, он закрывается.<br>
**Пожертвования**<br>
Пользователи могут совершать пожертвования и оставлять комментарии к ним. Все средства сначала поступают в общий фонд, а затем распределяются по текущим проектам.<br>
**Пользователи**<br>
Создание целевых проектов осуществляется администраторами сайта. Однако каждый пользователь может просмотреть полный список проектов и сделанных вкладов.

----
### <anchor>Техническая информация</anchor>
API приложения соответствует стандартам _Openapi_
Документация по API доступна по адресу: `127.0.0.1:8000/docs` и `127.0.0.1:8000/redoc`
API разделено на категории: _projects_, _donations_, _users_

**Проекты**
- Просмотр существующих проектов (_доступно всем_).
- Создавать, удалять и обновлять проекты могут только _администраторы (суперпользователи)_.

**Пожертвования**
- Просматривать существующие и создавать новые донаты могут все _зарегистрированные пользователи_.
- Каждый _зарегистрированный пользователь_ может просматривать свои созданные пожертвования.
- Удалять созданные пожертвования нельзя!

**Пользователи**
- *Зарегистрированные пользователи* могут просматривать информацию о себе, обновлять данные о себе.

----
### <anchor>Руководство по запуску</anchor>

1. Клонирование репозитория:<br>
`git clone git@github.com:kokos02r2/cat_charity_fund.git`<br>
Переход в директорию проекта: `cat_charity_fund`<br>

_Для Linux/macOS_<br>
2. Создание и активация виртуального окружения: <br>
`python3 -m venv venv` <br>
`source venv/bin/activate`<br>
3. Установка зависимостей: <br>
`python3 -m pip install --upgrade pip` <br>
 `pip install -r requirements.txt` <br>
4. Применение миграций:<br>
`alembic upgrade head`<br>
5. Запуск проекта:<br>
`uvicorn app.main:app --reload`

_Для Windows_<br>
2. Создание и активация виртуального окружения: <br>
`python -m venv venv` <br>
`source venv/scripts/activate` <br>
3. Установка зависимостей: <br>
`python -m pip install --upgrade pip` <br>
`pip install -r requirements.txt` <br>
4. Применение миграций:<br>
`alembic upgrade head`<br>
5. Запуск проекта:<br>
`uvicorn app.main:app --reload`
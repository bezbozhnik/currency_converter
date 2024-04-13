# Решение на тестовое задание от компании Айти Гуру.

# ТЗ:

## Написать сервис "Конвертер валют", который работает по REST-API.
- Пример запроса: `GET /api/rates?from=USD&to=RUB&value=1`
- Пример ответа: `{'result': 62.16}

# Запуск
- Клонируем репозиторий
`git clone https://github.com/bezbozhnik/currency_converter.git --config core.autocrlf=input`
- Запускаем в корневой папке проект:
`docker-compose -f .\docker-compose.yml up -d`
- Сервер будет доступен под URL-адресу `http://localhost:16000/api/`
- Swagger будет доступен по `http://localhost:16000/api/docs#/` | `http://localhost:16000/api/redocs#/`

# Стэк
- Python 3.12
- FastAPI ~=0.110.1

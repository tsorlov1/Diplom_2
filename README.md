## Дипломный проект. Задание 2: API

### Автотесты для проверки API заказа бургеров в Stellar Burgers

### Структура проекта

- `helpers` - пакет, содержащий: `helpers_order.py`, `helpers_user.py`
- `tests` - пакет, содержащий: `conftest.py`, `test_order_create.py`, `test_order_get_user.py`, `test_user_login.py`, `test_user_registration.py`, `test_user_update_data.py`
- `data.py` 
- `requirements.txt` 
- `README.md` 
### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**
> `$pytest -v ./tests`

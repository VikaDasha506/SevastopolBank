from celery import shared_task
import requests
from django.core.cache import cache


@shared_task
def fetch_exchange_rates():
    # Обновите URL, если базовая валюта - RUB
    url = 'https://v6.exchangerate-api.com/v6/c39ba5fc361ff2f7cda3b7b9/latest/RUB'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Кешируем данные на 3 часа (10800 секунд)
        cache.set('exchange_rates', data, timeout=10800)
        return data
    else:
        # Обработка ошибок или логирование
        print('Данные не доступны')


# Проверяем загрузку данных в кеш
# Запуск Django shell
# python manage.py shell

# В Django shell
# from bank.tasks import fetch_exchange_rates

# Вызов функции и вывод результата
# data = fetch_exchange_rates()
# print(data)


#  migrate && echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Manina_A', 'anka506@rambler.ru', 'Manynya506')" | python3 manage.py shell
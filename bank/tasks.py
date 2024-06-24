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
        print('Failed to fetch exchange rates')
       # Получаем данные из кеша
    # exchange_rates = cache.get('exchange_rates')
    #
    #     # Проверяем, есть ли данные
    # if exchange_rates:
    #     print(exchange_rates)
    # else:
    #     print('Данные о курсах валют отсутствуют в кеше.')

# python manage.py shell
# from django.core.cache import cache
#
# # Получаем данные из кеша
# exchange_rates = cache.get('exchange_rates')
#
# # Проверяем, есть ли данные
# if exchange_rates:
#     print(exchange_rates)
# else:
#     print('Данные о курсах валют отсутствуют в кеше.')
# from bank.tasks import fetch_exchange_rates
# fetch_exchange_rates()
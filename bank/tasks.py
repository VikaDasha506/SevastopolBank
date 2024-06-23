from celery import shared_task
import requests
from django.core.cache import cache


@shared_task
def fetch_exchange_rates():
    url = 'https://v6.exchangerate-api.com/v6/6e06364efafd152dd538f1b09c400e3b/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Кешируем данные на 3 часа (10800 секунд)
        cache.set('exchange_rates', data, timeout=10800)
    else:
        # Обработка ошибок или логирование
        print('Failed to fetch exchange rates')

        from django.core.cache import cache

        # Получаем данные из кеша
        exchange_rates = cache.get('exchange_rates')

        # Проверяем, есть ли данные
        if exchange_rates:
            print(exchange_rates)
        else:
            print('Данные о курсах валют отсутствуют в кеше.')
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

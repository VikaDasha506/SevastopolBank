"""Вьюха для информационной панели"""
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup
from django.core.cache import cache


# Create your views here.
def main(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'base.html')


class AboutFizView(TemplateView):
    """Вьюшка для статики. Но можно при желании добавить динамический контент"""
    template_name = 'face_fiz.html'
    extra_context = {'title': 'О кредитах'}  # Обновляется только при загрузке Сервера


class IndexView(TemplateView):
    """наследует от MenuMixin и TemplateView.
     Oсновная страница. Шаблон 'main.html'."""
    template_name = 'main_content.html'


def get_credit(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit.html')


def get_deposits(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'deposits.html')


def get_cards(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'cards.html')


def get_invoices_transfers(request):
    return render(request, 'invoices_transfers.html')


def get_securities(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'accounts_securities.html')


def get_additional_services(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'additional_services.html')


def get_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'mortgage.html')


def get_consumer_credit(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'consumer_credit.html')


def get_credit_card(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit_card.html')


def get_credit_holidays(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'credit_holidays.html')


def get_government_support(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'government_support.html')


def get_military_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'military_mortgage.html')


def get_it_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'it_mortgage.html')


def get_family_mortgage(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'family_mortgage.html')


from django.views.generic import View
from bank.tasks import fetch_exchange_rates  # Убедитесь, что задача импортирована правильно


class ExchangeRateView(View):
    template_name = 'currency.html'

    def get(self, request, *args, **kwargs):
        # Проверяем, есть ли данные в кеше
        exchange_rates = cache.get('exchange_rates')
        if not exchange_rates:
            # Если данных нет, вызываем задачу для их получения
            fetch_exchange_rates.delay()
            # Можно добавить сообщение пользователю о том, что данные обновляются
            context = {
                'message': 'Данные о курсах валют обновляются. Пожалуйста, обновите страницу через некоторое время.'}
        else:
            # Если данные есть, передаем их в контекст
            context = {'exchange_rates': exchange_rates}

        return render(request, self.template_name, context)


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     # Получаем данные из кеша
#     exchange_rates = cache.get('exchange_rates')
#     # Проверяем, что данные существуют и имеют правильный формат
#     if exchange_rates and 'conversion_rates' in exchange_rates:
#         context['exchange_rates'] = exchange_rates['conversion_rates']
#         # Выводим данные на печать для проверки
#         print(exchange_rates['conversion_rates'])
#     return context

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     # Получаем данные из кеша
#     exchange_rates = cache.get('exchange_rates')
#     # Проверяем, что данные существуют и имеют правильный формат
#     if exchange_rates and 'conversion_rates' in exchange_rates:
#         context['exchange_rates'] = exchange_rates['conversion_rates']
#         # Выводим данные на печать для проверки
#         print(exchange_rates['conversion_rates'])
#     return context


# class ExchangeRateView(TemplateView):
#     template_name = 'currency.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Получаем данные из кеша
#         exchange_rates = cache.get('exchange_rates')
#         context['exchange_rates'] = exchange_rates
#         return context


# Dollar_rub = ('https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw:1584716087546&source='
#               'hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%'
#               'D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.'
#               '3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4')
# title = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.'
#                   '0.0 Safari/537.36 Edg/125.0.0.0'}
#
#
# class Currency():
#     template_name = 'currency.html'
#     DOLLAR_RUB = Dollar_rub
#     headers = title
#     current_converted_price = 0
#
#     def __init__(self):
#         self.current_converted_price = self.get_currency_price().replace(",", ".")
#
#     def get_currency_price(self):
#         full_page = requests.get(self.DOLLAR_RUB, headers=self.headers)
#         """Создаем запрос по нужному URL.Передаем данные DOLLAR_RUB,headers для обработки"""
#
#         soup = BeautifulSoup(full_page.content, 'html.parser')
#         convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
#         # находим в консоли разработчика на сайте (гугл DOLLAR_RUB) все тэги подходящие под нащ запрос,
#         # в нашем случае нужны все "span" с их классами "class".
#         # Ищем все тэги span из разметки
#         convert_doll = convert[0].text
#         print(convert_doll)
#         return convert_doll
#
#     # def check_currency(self):
#     # """Обновление курса"""
#     #     currency = float(self.get_currency_price().replace(",", "."))
#     #     time.sleep(3)
#     #     self.check_currency()
#
#     #
#     def __str__(self):
#         return f" {self.current_converted_price}"
#
#
# # !!! Передать из представления currency в контекст шаблона currency.html
# def currency_view(request):
#     currency = Currency()
#     context = {
#         'current_converted_price': currency.current_converted_price
#     }
#     return render(request, 'currency.html', context)
# Функция для получения курса валюты
# def get_currency_rate():
#     # Адрес сайта, с которого мы будем получать данные
#     url = "https://www.google.com/search?q=курс+доллара+к+рублю"
#
#     # Получаем содержимое страницы
#     response = requests.get(url)
#
#     # Создаем объект BeautifulSoup для парсинга HTML-разметки
#     soup = BeautifulSoup(response.content, "html.parser")
#
#     # Получаем элемент с курсом валюты
#     result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
#
#     # Возвращаем курс валюты как число
#     return str(result.replace(",", "."))
#
#
# # Основной код программы
# if __name__ == "__main__":
#     # Получаем текущий курс валюты
#     current_rate = get_currency_rate()
#     # print(current_rate)

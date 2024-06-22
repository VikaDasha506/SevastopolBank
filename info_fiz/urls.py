"""
URL configuration for anki project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from anki import settings
# from cards import views
# from django.views.decorators.cache import cache_page
#
# loan_application.site.site_header = 'Управление моим сайтом'  # Текст в шапке
# loan_application.site.site_title = 'Административный сайт'  # Текст в титле
# loan_application.site.index_title = 'Добро пожаловать в панель управления' # Текст на главной странице
#

from django.urls import path
from . import views

app_name = 'info_fiz'  # Пространство имен для приложения

urlpatterns = [
    path('credit/', views.get_credit, name='credit'),  # Информация по кредитованию физически х лиц
    path('deposits/', views.get_deposits, name='deposits'),  # Информация по депозитам
    path('cards/', views.get_cards, name='cards'),  # Информация по картам
    path('invoices_transfers/', views.get_invoices_transfers, name='invoices_transfers'),
    # Информация по счетам и переводам
    path('securities/', views.get_securities, name='securities'),  # Информация по ценным бумагам
    path('additional_services/', views.get_additional_services, name='additional_services'),
    # Информация по дополнительным услугам
    path('credit/mortgage/', views.get_mortgage, name='mortgage'),  # Информация по ипотеке
    path('credit/credit_card/', views.get_credit_card, name='credit_card'),  # Информация по кредитной карте
    path('credit/consumer_credit/', views.get_consumer_credit, name='consumer_credit'),
    # Информация по потребительскоу кредиту
    path('credit/credit_holidays/', views.get_credit_holidays, name='credit_holidays'),
    # Информация по кредитным каникулам
    path('credit/mortgage/government_support/', views.get_government_support, name='government_support'),
    # Информация по ипотеке с гос.поддержкой
    path('credit/mortgage/military_mortgage/', views.get_military_mortgage, name='military_mortgage'),
    # Информация по военной ипотеке
    path('credit/mortgage/it_mortgage/', views.get_it_mortgage, name='it_mortgage'),  # Информация по it-ипотеке
    path('credit/mortgage/family_mortgage/', views.get_family_mortgage, name='family_mortgage'),
    # Информация по семейной ипотеке
    path('exchange-rates/', (views.ExchangeRateView.as_view()), name='exchange_rates'),


]#celery A bank loglevel=info celery -A bank -loglevel=info
#celery -A bank worker --loglevel=info
#celery -A bank beat --loglevel=info
#sudo apt-get install redis-serverworker -A bank --loglevel=debug --concurrency=2

# При запуске Celery командой celery -A bank worker --loglevel=info постоянно ошибка ERROR/MainProcess] consumer: Cannot connect to redis://127.0.0.1:6379/0: Error 10061 connecting to 127.0.0.1:6379. Подключение не установлено, т.к. конечный компьютер отверг запрос на подключение..
# Trying again in 6.00 seconds... (3/100)
# . Уже не знаю,что делать. Ругается на redit
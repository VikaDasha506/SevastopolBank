from django.urls import path
from . import views

app_name = 'history'  # Пространство имен для приложения

urlpatterns = [
    path('history/', (views.AboutBankView.as_view()), name='about'),
]
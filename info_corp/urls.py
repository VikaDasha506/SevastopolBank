from django.urls import path
from . import views

app_name = 'info_corp'  # Пространство имен для приложения

urlpatterns = [
    path('salary_project/', views.get_salary_project, name='salary_project'),  # Информация по зарплатному проекту
    path('acquiring/', views.get_acquiring, name='acquiring'),  # Информация по Эквайрингу и СБП
    path('cash_settlement_services/', views.get_cash_settlement_services, name='cash_settlement_services'),
    # Информация по Расчетно-кассовому обслуживанию (РКО)
    path('crediting/', views.get_crediting, name='crediting'),  # Информация по кредитованию юридических лиц
    path('placement_funds/', views.get_placement_funds, name='placement_funds'),
    # Информация по размещению денежных средств
]

from django.shortcuts import render

# Create your views here.
"""Вьюха для информационной панели"""

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# <li><a class="dropdown-item" href="#">Зарплатный проект</a></li>
#         <li><a class="dropdown-item" href="#">Эквайринг и СБП</a></li>
#         <li><a class="dropdown-item" href="#">Расчетно-кассовое обслуживание (РКО)</a>
#         <li><a class="dropdown-item" href="#">Кредитование</a></li>
#         <li><a class="dropdown-item" href="#">Размещение денежных средств</a></li>
# Create your views here.
def get_salary_project(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'salary_project.html')


def get_acquiring(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'acquiring.html')


def get_cash_settlement_services(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'cash_settlement_services.html')


def get_crediting(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'crediting.html')


def get_placement_funds(request):
    """Представление рендерит шаблон base.html"""
    return render(request, 'placement_funds.html')

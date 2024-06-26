"""
URL configuration for bank project.

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
from django.contrib import admin
from django.urls import path, include
from info_fiz import views

admin.site.site_header = 'Управление моим сайтом'  # Текст в шапке
admin.site.site_title = 'Административный сайт'  # Текст в титле
admin.site.index_title = 'Добро пожаловать в панель управления'  # Текст на главной странице

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', (views.IndexView.as_view()), name='index'),
    path('fiz/', include('info_fiz.urls', namespace='fiz')),
    path('corp/', include('info_corp.urls', namespace='corp')),
    path('user/', include('user.urls', namespace='user')),
    path('history/', include('history.urls', namespace='history')),
]

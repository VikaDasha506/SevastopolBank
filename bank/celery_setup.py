from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


#Задаём настройки Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bank.settings')
app = Celery('bank')

#Используем конфигурации Django
app.config_from_object('django.conf:settings', namespace='CELERY')

#Автоматически искать задачи в приложениях Django
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'fetch-exchange-rates-every-3-hours': {
        'task': 'bank.tasks.fetch_exchange_rates',
        'schedule': crontab(minute=0, hour='*/3'),
    },
}
# Запустите Celery worker и beat:
# celery -A bank worker --loglevel=info
# celery -A bank beat --loglevel=info
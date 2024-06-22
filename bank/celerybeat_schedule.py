from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'fetch-exchange-rates-every-3-hours': {
        'task': 'currency_app.tasks.fetch_exchange_rates',
        'schedule': crontab(minute=0, hour='*/3'),
    },
}

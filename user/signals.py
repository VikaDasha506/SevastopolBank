from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from user.models import Feedback, LoanApplication
from user.telegram_bot import send_telegram_message
import os


@receiver(post_save, sender=Feedback)
def notify_admin_sync(sender, instance, created, **kwargs):
    if created:
        message = f'Получено новое сообщение от клиента: {instance.name}.'
        async_to_sync(send_telegram_message)(
            os.getenv("TELEGRAM_BOT_TOKEN"),
            os.getenv("YOUR_PERSONAL_CHAT_ID"),
            message,
            parse_mode="HTML"
        )


@receiver(post_save, sender=LoanApplication)
def notify_admin_sync(sender, instance, created, **kwargs):
    if created:
        message = f'Получена новая заявка: {instance.customer} от клиента: {instance.name}.'
        async_to_sync(send_telegram_message)(
            os.getenv("TELEGRAM_BOT_TOKEN"),
            os.getenv("YOUR_PERSONAL_CHAT_ID"),
            message,
            parse_mode="HTML")

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TelegramSenderConfig(AppConfig):
    name = 'telegram_sender'
    verbose_name = _('Telegram Sender')

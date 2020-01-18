from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Bot(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=128)
    telegram_token = models.CharField(verbose_name=_('telegram token'),
                                      max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name=_('user'), related_name='bots')

    def __str__(self) -> str:
        return self.name


class ApiToken(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=128)
    token = models.CharField(verbose_name=_('token'), max_length=128)
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE,
                            verbose_name=_('bot'), related_name='api_tokens')

    def __str__(self) -> str:
        return self.name

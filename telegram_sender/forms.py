from django import forms

from telegram_sender.models import Bot


class SimpleBotAdminForm(forms.ModelForm):
    class Meta:
        model = Bot
        exclude = 'user',

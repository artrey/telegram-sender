from django import forms

from telegram.models import Bot


class SimpleBotAdminForm(forms.ModelForm):
    class Meta:
        model = Bot
        exclude = 'user',

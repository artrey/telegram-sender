from django import forms

from telegram_sender.models import Bot


class SimpleBotAdminForm(forms.ModelForm):
    class Meta:
        model = Bot
        exclude = 'user',


class BotInjectedForm(forms.Form):
    bot = forms.ModelChoiceField(Bot.objects.none(),
                                 required=True, empty_label=None)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bot'].queryset = Bot.objects.filter(user=user)


class TestSendForm(BotInjectedForm):
    chat_id = forms.CharField(required=True)
    message = forms.CharField(required=True)

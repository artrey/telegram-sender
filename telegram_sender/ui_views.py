from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _

from telegram_sender.forms import TestSendForm, BotInjectedForm
from utils.telegram_helper import send_message, get_updates


class BotInjectedView(FormView):
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TestSendView(LoginRequiredMixin, BotInjectedView):
    template_name = 'telegram_sender/test_send.html'
    form_class = TestSendForm
    extra_context = {'title': _('Test send')}

    def form_valid(self, form):
        context = self.get_context_data()
        try:
            context['result'] = send_message(
                form.cleaned_data['bot'].telegram_token,
                form.cleaned_data['chat_id'],
                form.cleaned_data['message']
            )
        except Exception as ex:
            context['error'] = str(ex)
        return render(self.request, self.template_name, context)


class GetChatIdView(LoginRequiredMixin, BotInjectedView):
    template_name = 'telegram_sender/get_chat_id.html'
    form_class = BotInjectedForm
    extra_context = {'title': _('Get chat id')}

    def form_valid(self, form):
        context = self.get_context_data()
        try:
            context['result'] = get_updates(
                form.cleaned_data['bot'].telegram_token
            )
        except Exception as ex:
            context['error'] = str(ex)
        return render(self.request, self.template_name, context)

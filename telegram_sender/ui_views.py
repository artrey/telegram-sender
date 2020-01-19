from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, FormView

from telegram_sender.exceptions import *
from telegram_sender.forms import TestSendForm
from telegram_sender.models import ApiToken, Bot
from telegram_sender.responses import valid_response


class TestSendView(LoginRequiredMixin, FormView):
    template_name = 'telegram_sender/test_send.html'
    form_class = TestSendForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print('valid')
        return super().form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['bots'] = Bot.objects.filter(user=self.request.user)
    #     return context

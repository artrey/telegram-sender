from django.views import View

from telegram_sender.exceptions import exceptions_handle
from telegram_sender.responses import valid_response
from telegram_sender.telegram_helper import send_message_via_api_token


class SendView(View):
    @exceptions_handle
    def post(self, request):
        send_message_via_api_token(request.POST)
        return valid_response({})

    @exceptions_handle
    def get(self, request):
        send_message_via_api_token(request.GET)
        return valid_response({})

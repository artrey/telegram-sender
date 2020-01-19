from django.views import View

import telegram

from telegram_sender.exceptions import *
from telegram_sender.models import ApiToken
from telegram_sender.responses import valid_response


def check_or_raise(value, error_type):
    if not value:
        raise error_type()
    return value


def extract_credentials(context: dict) -> (str, str, str):
    tok = check_or_raise(context.get('tok'), TokenNotProvidedException)
    api_token = check_or_raise(ApiToken.objects.filter(token=tok).first(),
                               TokenNotExistsException)
    cid = check_or_raise(context.get('cid'), ChatIdNotProvidedException)
    mes = check_or_raise(context.get('mes'), MessageNotProvidedException)
    return api_token.bot.telegram_token, cid, mes


def send_message(context: dict) -> None:
    token, chat_id, message = extract_credentials(context)
    # telegram.Bot(token=token).send_message(chat_id=chat_id, text=message)
    print(token, chat_id, message)


class SendView(View):
    @exceptions_handle
    def post(self, request):
        send_message(request.POST)
        return valid_response({})

    @exceptions_handle
    def get(self, request):
        send_message(request.GET)
        return valid_response({})

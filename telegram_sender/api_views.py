from telegram import Message

from django.views import View

from telegram_sender.responses import valid_response
from utils.telegram_helper import send_message
from telegram_sender.exceptions import *
from telegram_sender.models import ApiToken
from utils.check_or_raise import check_or_raise


def extract_credentials(context: dict) -> (str, str, str):
    tok = check_or_raise(context.get('tok'), TokenNotProvidedException)
    api_token = check_or_raise(ApiToken.objects.filter(token=tok).first(),
                               TokenNotExistsException)
    cid = check_or_raise(context.get('cid'), ChatIdNotProvidedException)
    mes = check_or_raise(context.get('mes'), MessageNotProvidedException)
    return api_token.bot.telegram_token, cid, mes


def send_message_via_api_token(context: dict) -> Message:
    return send_message(*extract_credentials(context))


class SendView(View):
    @exceptions_handle
    def post(self, request):
        send_message_via_api_token(request.POST)
        return valid_response({})

    # @exceptions_handle
    # def get(self, request):
    #     send_message_via_api_token(request.GET)
    #     return valid_response({})

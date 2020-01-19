import telegram

from telegram_sender.exceptions import *
from telegram_sender.models import ApiToken
from utils.check_or_raise import check_or_raise


def send_message(token: str, chat_id: str, message: str) -> None:
    # telegram.Bot(token=token).send_message(chat_id=chat_id, text=message)
    print(token, chat_id, message)


def extract_credentials(context: dict) -> (str, str, str):
    tok = check_or_raise(context.get('tok'), TokenNotProvidedException)
    api_token = check_or_raise(ApiToken.objects.filter(token=tok).first(),
                               TokenNotExistsException)
    cid = check_or_raise(context.get('cid'), ChatIdNotProvidedException)
    mes = check_or_raise(context.get('mes'), MessageNotProvidedException)
    return api_token.bot.telegram_token, cid, mes


def send_message_via_api_token(context: dict) -> None:
    send_message(*extract_credentials(context))

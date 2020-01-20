import telegram
from telegram import Message, Update


def send_message(token: str, chat_id: str, message: str) -> Message:
    return telegram.Bot(token=token).send_message(chat_id=chat_id, text=message)


def get_updates(token: str) -> Update:
    return telegram.Bot(token=token).get_updates()

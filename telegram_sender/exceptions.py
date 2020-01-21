import functools

from django.utils.translation import gettext_lazy as _

from .responses import invalid_response


class TelegramSenderException(Exception):
    message = _('General telegram sender exception')
    __code = None

    @property
    def code(self) -> str:
        if not self.__class__.__code:
            self.__class__.__code = self.__class__.__name__
            if self.__class__.__code.lower().endswith('exception'):
                self.__class__.__code = self.__class__.__code[:-9]
        return self.__class__.__code

    def __str__(self) -> str:
        return self.message


class TokenNotProvidedException(TelegramSenderException):
    message = _('Token is not provided in request')


class TokenNotExistsException(TelegramSenderException):
    message = _('Token is not exists or deactivated')


class ChatIdNotProvidedException(TelegramSenderException):
    message = _('Chat id is not provided in request')


class MessageNotProvidedException(TelegramSenderException):
    message = _('Message is not provided in request')


def exceptions_handle(view: callable) -> callable:
    @functools.wraps(view)
    def wrapper(*args, **kwargs):
        try:
            return view(*args, **kwargs)
        except TelegramSenderException as ex:
            return invalid_response({'reason': ex.message, 'code': ex.code})
        except Exception as ex:
            return invalid_response({'reason': str(ex), 'code': 'UNKNOWN'})
    return wrapper

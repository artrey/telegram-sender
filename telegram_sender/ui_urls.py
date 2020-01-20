from django.urls import path

from telegram_sender.ui_views import TestSendView, GetChatIdView

urlpatterns = [
    path('', TestSendView.as_view(), name='test_send'),
    path('get_chat_id/', GetChatIdView.as_view(), name='get_chat_id'),
]

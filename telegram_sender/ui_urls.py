from django.urls import path

from telegram_sender.ui_views import TestSendView

urlpatterns = [
    path('', TestSendView.as_view(), name='test_send'),
]

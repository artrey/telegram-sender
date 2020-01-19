from django.urls import path

from telegram_sender.api_views import SendView

urlpatterns = [
    path('send/', SendView.as_view(), name='send'),
]

from django.urls import path

from telegram.views import send_view

urlpatterns = [
    path('send/', send_view, name='send'),
]

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class AdminSite(admin.AdminSite):
    site_header = _('Telegram sender')
    site_title = _('Telegram sender')
    index_title = _('Configuration page')

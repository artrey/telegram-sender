from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class AdminSite(admin.AdminSite):
    site_header = _('Telegram sender')
    site_title = _('Telegram sender site admin')
    index_title = None

from django.contrib import admin
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

import utils
from telegram_sender.forms import SimpleBotAdminForm
from telegram_sender.models import Bot, ApiToken


class ApiTokenInline(admin.TabularInline):
    model = ApiToken
    extra = 0
    readonly_fields = 'token',


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = 'name', 'telegram_token', 'api_tokens_count',
    inlines = ApiTokenInline,

    def api_tokens_count(self, obj) -> int:
        return obj.api_tokens_count
    api_tokens_count.short_description = _('api tokens count')
    api_tokens_count.admin_order_field = 'api_tokens_count'

    def get_queryset(self, request):
        qs = super(BotAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(user=request.user)
        return qs.annotate(api_tokens_count=Count('api_tokens'))

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            kwargs['form'] = SimpleBotAdminForm
        return super().get_form(request, obj, **kwargs)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save()
        for instance in instances:
            if not instance.token:
                instance.token = utils.generate_password(32)
            instance.save()

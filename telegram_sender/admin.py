from django.contrib import admin

import utils
from telegram_sender.forms import SimpleBotAdminForm
from telegram_sender.models import Bot, ApiToken


class ApiTokenInline(admin.TabularInline):
    model = ApiToken
    extra = 0
    readonly_fields = 'token',


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    inlines = ApiTokenInline,

    def get_queryset(self, request):
        qs = super(BotAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

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

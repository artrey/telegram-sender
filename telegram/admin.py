from django.contrib import admin

from telegram.forms import SimpleBotAdminForm
from telegram.models import Bot, ApiToken


class ApiTokenInline(admin.TabularInline):
    model = ApiToken
    extra = 0


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
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

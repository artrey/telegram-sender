from django.contrib import admin

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

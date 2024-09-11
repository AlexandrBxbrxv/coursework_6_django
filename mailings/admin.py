from django.contrib import admin

from mailings.models import Client


@admin.register(Client)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name',)
    search_fields = ('full_name',)

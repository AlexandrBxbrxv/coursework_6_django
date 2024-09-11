from django.contrib import admin

from mailings.models import ServiceClient


@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name',)
    search_fields = ('full_name',)

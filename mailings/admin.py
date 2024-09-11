from django.contrib import admin

from mailings.models import Client, MailingMessage


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name',)
    search_fields = ('full_name',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'msg_topic',)
    search_fields = ('msg_topic',)

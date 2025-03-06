from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import HomeTemplateView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView, MailingMessageListView, MailingMessageDetailView, MailingMessageCreateView, \
    MailingMessageUpdateView, MailingMessageDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('clients', ClientListView.as_view(), name='clients'),
    path('client/<int:pk>/detail', ClientDetailView.as_view(), name='client_detail'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name='client_delete'),
    path('mailing_messages/create', MailingMessageCreateView.as_view(), name='mailing_message_create'),
    path('mailing_messages', MailingMessageListView.as_view(), name='mailing_messages'),
    path('mailing_messages/<int:pk>/detail', MailingMessageDetailView.as_view(), name='mailing_message_detail'),
    path('mailing_messages/<int:pk>/update', MailingMessageUpdateView.as_view(), name='mailing_message_update'),
    path('mailing_messages/<int:pk>/delete', MailingMessageDeleteView.as_view(), name='mailing_message_delete'),
]

from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import HomeTemplateView, ClientListView

app_name = MailingsConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('clients', ClientListView.as_view(), name='clients'),
]

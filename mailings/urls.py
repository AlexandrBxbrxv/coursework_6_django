from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import HomeTemplateView, ClientListView, ClientDetailView

app_name = MailingsConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('clients', ClientListView.as_view(), name='clients'),
    path('client<int:pk>/detail', ClientDetailView.as_view(), name='client_detail'),
]

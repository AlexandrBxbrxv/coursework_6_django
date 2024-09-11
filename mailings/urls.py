from django.urls import path
from mailings.apps import MailingsConfig

from mailings.views import HomeTemplateView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, \
    ClientDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('clients', ClientListView.as_view(), name='clients'),
    path('client<int:pk>/detail', ClientDetailView.as_view(), name='client_detail'),
    path('client<int:pk>/update', ClientUpdateView.as_view(), name='client_update'),
    path('client<int:pk>/delete', ClientDeleteView.as_view(), name='client_delete'),
]

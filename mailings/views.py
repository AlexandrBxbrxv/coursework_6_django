from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from mailings.models import Client


class HomeTemplateView(TemplateView):
    template_name = 'mailings/home.html'


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'full_name', 'comment',)
    success_url = reverse_lazy('mailings:clients')


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client

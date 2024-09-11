from django.views.generic import TemplateView, ListView

from mailings.models import Client


class HomeTemplateView(TemplateView):
    template_name = 'mailings/home.html'


class ClientListView(ListView):
    model = Client

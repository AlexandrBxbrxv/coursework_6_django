from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.models import Client, MailingMessage


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


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('email', 'full_name', 'comment',)

    def get_success_url(self):
        return reverse('mailings:client_detail', args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailings:clients')


class MailingMessageListView(ListView):
    model = MailingMessage

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Сообщения для рассылки'})
        return context


class MailingMessageDetailView(DetailView):
    model = MailingMessage


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    fields = ('msg_topic', 'msg_body',)
    success_url = reverse_lazy('mailings:mailing_messages')


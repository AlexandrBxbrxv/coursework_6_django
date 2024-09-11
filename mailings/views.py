from django.views.generic import TemplateView

from mailings.apps import MailingsConfig

app_name = MailingsConfig.name


class HomeTemplateView(TemplateView):
    template_name = 'mailings/home.html'

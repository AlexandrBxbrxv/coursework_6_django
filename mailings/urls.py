from django.urls import path

from mailings.views import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
]

from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='email', help_text='обязательное поле')
    full_name = models.CharField(max_length=200, verbose_name='Ф.И.О.', help_text='обязательное поле')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    class Meta:
        verbose_name = 'клиент сервиса'
        verbose_name_plural = 'клиенты сервиса'
        ordering = ('full_name',)

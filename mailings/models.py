from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='email')
    full_name = models.CharField(max_length=200, verbose_name='Ф.И.О.')
    comment = models.TextField(**NULLABLE, verbose_name='комментарий')

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('full_name',)


class MailingMessage(models.Model):
    msg_topic = models.CharField(max_length=100, verbose_name='тема')
    msg_body = models.TextField(verbose_name='содержимое')

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения для рассылок'
        ordering = ('msg_topic',)

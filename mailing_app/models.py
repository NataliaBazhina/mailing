from django.db import models
from clients_app.models import Client

class Mail(models.Model):
    topic = models.CharField(max_length=35, verbose_name='тема письма')
    content = models.TextField(verbose_name='тело письма')


class Mailing(models.Model):
    first_mailing = models.DateTimeField(verbose_name='первая рассылка',null=True, blank=True)
    periodicity = models.PositiveBigIntegerField(verbose_name='переодичность', default=60)
    status = models.CharField(max_length=35, verbose_name='статус')
    clients = models.ManyToManyField(Client)
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)

class MailingTrying(models.Model):
    last_mailing = models.DateTimeField(verbose_name='последняя рассылка')
    status_trying = models.BooleanField()
    server_response = models.CharField(max_length=35)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, null=True, blank=True)
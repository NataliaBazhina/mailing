from datetime import datetime, timedelta

from django.conf import settings
from django.utils import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Mailing, MailingTrying, Client
from django.core.mail import send_mail


def check_and_send_mailings():
    mailings = Mailing.objects.filter(status=Mailing.Status.CREATED, first_mailing__lte=timezone.now())

    for mailing in mailings:
        if mailing.first_mailing and (timezone.now() - mailing.first_mailing).total_seconds() >= mailing.periodicity:
            mailing.status = Mailing.Status.RUNNING
            mailing.save()

            clients = mailing.clients.all()
            mail_subject = mailing.mail.topic
            mail_content = mailing.mail.content

            for client in clients:
                send_mail(
                    mail_subject,
                    mail_content,
                    settings.EMAIL_HOST_USER,
                    [client.email],
                    fail_silently=False,
                )

            MailingTrying.objects.create(
                last_mailing=timezone.now(),
                status_trying=True,
                server_response="Письма отправлены",
                mailing=mailing
            )

            mailing.first_mailing = timezone.now() + timedelta(minutes=mailing.periodicity)
            mailing.status = Mailing.Status.CREATED
            mailing.save()

            print(f"Рассылка для {mailing} была успешно отправлена.")
        else:
            print(f"Рассылка {mailing} не готова к отправке.")


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(check_and_send_mailings, 'interval', minutes=1)
    scheduler.start()

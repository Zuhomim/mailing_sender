from datetime import timedelta, datetime

import pytz
from django.core.mail import send_mail

from config import settings
from mailing.models import Mailing, Logs


def my_job():
    day = timedelta(days=1, hours=0, minutes=0)
    weak = timedelta(days=7, hours=0, minutes=0)
    month = timedelta(days=30, hours=0, minutes=0)
    datetime_now = datetime.now(pytz.timezone('Europe/Moscow'))
    mailings = Mailing.objects.all()
    for mail in mailings:
        if mail.start_date < datetime_now:
            mail.status = 'Запущена'
            mail.save()
            email = [mail.message.user.email]
            send_mail(
                subject=mail.message.title,
                message=mail.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email,
                fail_silently=False,
            )

            log = Logs(message=mail.message, status=mail.status)
            log.save()

            if mail.periodicity == 'ежедневно':
                mail.start_date = log.attempt_time + day
            elif mail.periodicity == 'еженедельно':
                mail.start_date_date = log.attempt_time + weak
            elif mail.periodicity == 'ежемесячно':
                mail.start_date_date = log.attempt_time + month

            if mail.start_date_date < mail.end_date:
                mail.status = 'Создана'
            else:
                mail.status = 'Завершена'
            mail.save()

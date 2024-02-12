from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from config import settings
from config.settings import DEFAULT_FROM_EMAIL
from mailing.utils import EmailSender

# scheduler = BackgroundScheduler()
# scheduler.add_jobstore(DjangoJobStore, "default")


class MailingTask:

    @classmethod
    def start(cls):
        cls.scheduler = BackgroundScheduler()
        cls.scheduler.add_jobstore(DjangoJobStore(), "default")
        cls.scheduler.start()

        cls.scheduler.add_job(
            cls.send_emails,
            trigger=CronTrigger(second="*/20"),
            id="send_emails_job",
            replace_existing=True
        )

    @classmethod
    def send_emails(cls):
        subject = "Test"
        message = "Test"
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = ["das.python@yandex.ru"]

        email_sender = EmailSender(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
        )
        email_sender.send()

    @classmethod
    def stop_send(cls):
        cls.scheduler.remove_job("send_emails_job")

    @staticmethod
    def handle_send_emails(request):
        MailingTask.start()
        MailingTask.send_emails()

from django_apscheduler.jobstores import DjangoJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore, "default")


class MailingTask:

    @classmethod
    def start(cls):
        cls.scheduler = BackgroundScheduler()
        cls.scheduler.add_jobstore(DjangoJobStore, "default")
        cls.scheduler.start()

        cls.scheduler.add_job(
            cls.send_emails,
            trigger=CronTrigger(second="*/600"),
            id="send_emails_job",
            replace_existing=True,
        )

    @classmethod
    def send_emails(cls):
        subject = ""
        message = ""
        from_email = ""
        recipient_list = []

        email_sender = EmailSender(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
        )
        email_sender.send()

    @classmethod
    def stop_send(cls):
        cls.scheduler.remove_job("send_emails_job")
from django.db import models
from django.db.models import Q

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    title = models.CharField(max_length=60, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма", **NULLABLE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Mailing(models.Model):
    time = models.DateTimeField(verbose_name="Дата рассылки")
    periodicity = models.CharField(max_length=30, choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'),
                                                           ('monthly', 'Ежемесячно')], verbose_name="Периодичность")
    status = models.CharField(max_length=30,
                              choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')],
                              verbose_name="Статус")
    user = models.ManyToManyField(User, verbose_name="Пользователь")
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"


class Logs(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    attempt_time = models.DateTimeField(verbose_name="Дата последней попытки")
    status = models.CharField(max_length=60, verbose_name="Статус")
    response = models.TextField(**NULLABLE, verbose_name="Ответ сервера")

    class Meta:
        verbose_name = "лог"

        verbose_name_plural = "логи"

        constraints = [
            models.CheckConstraint(
                name='not_empty_response_on_failure',
                check=Q(status=False, response__isnull=False) | Q(status=True),
            )
        ]

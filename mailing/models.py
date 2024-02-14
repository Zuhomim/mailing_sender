from django.db import models
from django.db.models import Q

import users
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    full_name = models.CharField(max_length=60, verbose_name='ФИО')
    email = models.EmailField(verbose_name='Почта')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    user = models.ForeignKey(users.models.User, on_delete=models.CASCADE, null=True, verbose_name='Менеджер')

    def __str__(self):
        return f'{self.email} ({self.full_name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=60, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма", **NULLABLE)
    user = models.ForeignKey(Client, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f'{self.title} ({self.body[:20]})'


class Mailing(models.Model):
    start_date = models.DateTimeField(verbose_name="Дата начала рассылки")
    end_date = models.DateTimeField(verbose_name="Дата завершения рассылки")
    periodicity = models.CharField(max_length=30, choices=[('daily', 'Ежедневно'), ('weekly', 'Еженедельно'),
                                                           ('monthly', 'Ежемесячно')], verbose_name="Периодичность")
    status = models.CharField(max_length=30,
                              choices=[('created', 'Создана'), ('started', 'Запущена'), ('completed', 'Завершена')],
                              verbose_name="Статус")
    user = models.ManyToManyField(Client, verbose_name="Пользователь")
    is_active = models.BooleanField(default=True, verbose_name="Статус")
    message = models.ForeignKey(Message, verbose_name="Сообщение", on_delete=models.SET_NULL, **NULLABLE)

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        permissions = [
            ('set_is_active', 'Can deactivate mailing')
        ]

    def __str__(self):
        return f'{self.start_date} - {self.end_date} ({self.periodicity}) - {self.status}'


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

    def __str__(self):
        return (f'{self.attempt_time}'
                f'{self.status}')

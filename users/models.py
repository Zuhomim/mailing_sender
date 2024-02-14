import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=60, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")
    is_active = models.BooleanField(default=True, verbose_name="Статус")
    uuid = models.CharField(primary_key=True, default=uuid.uuid4, editable=False, max_length=36)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email} ({self.full_name})'

    class Meta:
        permissions = [
            ("set_is_active", "Can block user"),
        ]

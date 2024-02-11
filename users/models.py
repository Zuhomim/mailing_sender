from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email")
    full_name = models.CharField(max_length=60, verbose_name="ФИО")
    comment = models.TextField(verbose_name="Комментарий")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
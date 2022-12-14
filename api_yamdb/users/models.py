from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    USER = 1
    ADMIN = 2
    MODERATOR = 3
    ROLE_CHOICES = (
        (USER, 'юзер'),
        (ADMIN, 'админ'),
        (MODERATOR, 'модератор'),
    )
    role = models.PositiveSmallIntegerField(
        'Роли',
        choices=ROLE_CHOICES,
        default=USER
    )

    bio = models.TextField(
        'Биография',
        blank=True,
    )

    class Meta:
        unique_together = ('username', 'email')

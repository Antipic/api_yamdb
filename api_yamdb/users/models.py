from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework_simplejwt.tokens import AccessToken
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    class UserRole(models.TextChoices):
        USER = 'user', _('Юзер')
        ADMIN = 'admin', _('Админ')
        MODERATOR = 'moderator', _('Модератор')

    role = models.CharField(
        'Роли',
        choices=UserRole.choices,
        default=UserRole.USER,
        max_length=10
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        db_index=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Недопустимый символ в имени пользователя!'
        )]
    )
    first_name = models.CharField('Имя', max_length=150, blank=True,)
    last_name = models.CharField('Фамилия', max_length=150, blank=True,)
    email = models.EmailField(
        'E-mail',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    user_token = models.CharField(
        'Токен',
        max_length=150,
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('username', 'email')

    def __str__(self):
        return self.username

    @property
    def token(self):
        return str(AccessToken.for_user(self))

    @property
    def is_admin(self):
        return self.role == self.UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.UserRole.MODERATOR

    @property
    def is_user(self):
        return self.role == self.UserRole.USER

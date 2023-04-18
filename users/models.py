from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, nickname, password, **extra_fields):
        if not nickname:
            raise ValueError('The nickname must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        user = self.model(nickname=nickname, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, nickname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('firstname', 'Admin')
        extra_fields.setdefault('lastname', 'Admin')
        extra_fields.setdefault('age', 16)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(nickname, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    nickname = models.CharField(max_length=255, unique=True, verbose_name='Никнейм')
    firstname = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    age = models.IntegerField(blank=True, validators=[MinValueValidator(11), MaxValueValidator(16)], verbose_name='Возраст')
    phone_number = models.CharField(blank=True, max_length=255, verbose_name='Номер телефона')
    password = models.TextField(verbose_name='Пароль')

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

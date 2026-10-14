from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_set',
        blank=True,
        help_text='NOMES DE USUARIOS QUE FAZ PARTE DESSE GRUPO',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',
        blank=True,
        help_text='PERMISAO ESPECIFICA PARA ESTE USUARIO',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

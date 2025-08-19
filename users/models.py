from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    second_name = models.CharField(null=True, blank=True)
    second_last_name = models.CharField(null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

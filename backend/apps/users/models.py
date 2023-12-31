from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField('Name of the User', blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    def __str__(self):
        return self.username

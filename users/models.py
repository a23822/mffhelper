from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False, blank=True)
    last_name = models.CharField(max_length=150, editable=False, blank=True)
    nickName = models.CharField(max_length=150, default="", unique=True)
    is_manager = models.BooleanField(default=False)
    aliance = models.ForeignKey(
        "aliances.Aliance", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return f"{self.nickName}"

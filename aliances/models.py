from django.db import models


class Aliance(models.Model):
    name = models.CharField(blank=True, max_length=100)
    member = models.ManyToManyField("users.User", related_name="member")

    def __str__(self):
        return f"{self.name}"

from django.db import models


class Hero(models.Model):

    index = models.PositiveSmallIntegerField()
    charIndex = models.PositiveSmallIntegerField(default=1)
    latestUniform = models.BooleanField(default=False)
    uniformName = models.CharField(max_length=50, default='')
    name = models.CharField(max_length=140)
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}:{self.uniformName}'

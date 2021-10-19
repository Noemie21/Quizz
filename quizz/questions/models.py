from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db.models.expressions import F


class User(AbstractUser):
    score = models.IntegerField(default=0)


class Question(models.Model):
    content = models.CharField(max_length=200)
    answer = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    howManyTime = models.IntegerField(default=2)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content

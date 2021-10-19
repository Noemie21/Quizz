from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import ModelState

class User(AbstractUser):
    score = models.IntegerField(default=0)
# Create your models here.


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=300, null=False, default=None)
    content = models.TextField(max_length=500, null=False, default=None)
    answer = models.CharField(max_length=100, null=False, default=None)
    time_asked = models.IntegerField(default=0)


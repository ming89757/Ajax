from django.db import models

# Create your models here.


class User(models.Model):
    uname = models.CharField(max_length=30, unique=True)
    upwd = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)

from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length = 20, null = False)
    password = models.CharField(max_length = 20, null = False)
    enabled = models.BooleanField(default = False)

    def __str__(self):
        return self.name


# Create your models here.

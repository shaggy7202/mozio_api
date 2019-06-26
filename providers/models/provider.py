from django.db import models
from django.contrib.auth.models import User


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=30)
    language = models.CharField(max_length=15)
    currency = models.CharField(max_length=15)

    def __str__(self):
        return self.name

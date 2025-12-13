from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class AuthUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    # password = models.CharField(max_length=128)
    # email = models.EmailField(unique=True)

    # def __str__(self):
    #     return self.username
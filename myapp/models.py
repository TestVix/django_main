from django.db import models
from django.contrib.auth.models import AbstractUser
import random
# Create your models here.
class AuthUser(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    # password = models.CharField(max_length=128)
    # email = models.EmailField(unique=True)

    # def __str__(self):
    #     return self.username
def get_unique_test_id():
    while True:
        number = random.randint(50000000, 90000000)
        if not Testlar.objects.filter(test_id=number).exists():
            return number

class Testlar(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    test_id = models.IntegerField(default=get_unique_test_id, unique=True)
    nom = models.CharField(max_length=100)
    fan = models.CharField(max_length=100)
    tavsif = models.TextField()
    public = models.BooleanField(default=True)
    def __str__(self):
        return self.nom
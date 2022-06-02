from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')

# Contactenos
class Contactenos(models.Model):
    name = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(null=False)
    comment = models.TextField(null=False)


# Nuestros Datos



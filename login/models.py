from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.jpg')
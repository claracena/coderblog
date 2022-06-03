from unicodedata import name
from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    info = models.TextField()
    updated = models.DateTimeField(auto_now=True)
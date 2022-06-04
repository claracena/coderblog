from unicodedata import name
from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=30)
    bday = models.DateField(null=True)
    info = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, default='avatar.jpg')
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    image = models.ImageField(null=True, default='avatar.jpg')
    updated = models.DateTimeField(auto_now=True)

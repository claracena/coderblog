from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.email
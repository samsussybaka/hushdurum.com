from django.db import models

# Create your models here.
class Email(models.Model):
    sender = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
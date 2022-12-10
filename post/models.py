from django.db import models
from email.message import EmailMessage
import ssl
import smtplib
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_date = models.DateField()
    
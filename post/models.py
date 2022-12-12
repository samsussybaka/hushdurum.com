from django.db import models
from email.message import EmailMessage
from django.utils.text import slugify
import ssl
import smtplib
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_date = models.DateField()
    url = models.SlugField(max_length=500, unique=True, blank=True, editable=False)
    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
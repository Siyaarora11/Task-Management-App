from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Page(models.Model):
    image = models.ImageField(upload_to='pics/')
class Register(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

class AddTask(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    deadline = models.DateTimeField(timezone.now() + timedelta(days=7))
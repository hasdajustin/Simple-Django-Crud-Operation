from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    list_display = ['username', 'phone', 'email']

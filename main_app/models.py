from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class Shopping_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.CharField(max_length=10)
    ingredient_name = models.CharField(max_length=255)


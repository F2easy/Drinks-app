from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ShoppingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredient_id = models.CharField(max_length=10)
    ingredient_name = models.CharField(max_length=255)


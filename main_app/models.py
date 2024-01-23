from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)


class Shopping_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    drink_id = models.CharField(max_length=20)
    drinkImage = models.CharField(max_length=255)
    ingredient_name = models.CharField(max_length=255)
    ingredient_1 = models.CharField(max_length=255)
    ingredient_2 = models.CharField(max_length=255)
    ingredient_3 = models.CharField(max_length=255)
    ingredient_4 = models.CharField(max_length=255)
    ingredient_5 = models.CharField(max_length=255)
    ingredient_6 = models.CharField(max_length=255)
    ingredient_7 = models.CharField(max_length=255)
    ingredient_8 = models.CharField(max_length=255)
    ingredient_9 = models.CharField(max_length=255)
    ingredient_10= models.CharField(max_length=255)
    ingredient_11= models.CharField(max_length=255)
    ingredient_12= models.CharField(max_length=255)
    ingredient_13= models.CharField(max_length=255)
    ingredient_14= models.CharField(max_length=255)
    ingredient_15= models.CharField(max_length=255)

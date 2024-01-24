from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class ShoppingGuide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    drink_id = models.CharField(max_length=20)
    drink_image = models.CharField(max_length=255)
    strIngredient1 = models.CharField(max_length=255, blank=True)
    strIngredient2 = models.CharField(max_length=255, blank=True)
    strIngredient3 = models.CharField(max_length=255, blank=True)
    strIngredient4 = models.CharField(max_length=255, blank=True)
    strIngredient5 = models.CharField(max_length=255, blank=True)
    strIngredient6 = models.CharField(max_length=255, blank=True)
    strIngredient7 = models.CharField(max_length=255, blank=True)
    strIngredient8 = models.CharField(max_length=255, blank=True)
    strIngredient9 = models.CharField(max_length=255, blank=True)
    strIngredient10 = models.CharField(max_length=255, blank=True)
    strIngredient11 = models.CharField(max_length=255, blank=True)
    strIngredient12 = models.CharField(max_length=255, blank=True)
    strIngredient13 = models.CharField(max_length=255, blank=True)
    strIngredient14 = models.CharField(max_length=255, blank=True)
    strIngredient15 = models.CharField(max_length=255, blank=True)
    
    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'list_id': self.id})
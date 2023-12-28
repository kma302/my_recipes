# recipes/models.py

from django.db import models
from django.contrib.auth.models import User
from image_cropping import ImageRatioField


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    recipe_by = models.CharField(max_length=200, default='Karen Arthur')
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='recipe_images')
    cropping = ImageRatioField('image', '200x200')

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    ingredients = models.ForeignKey(Recipe, on_delete=models.CASCADE)



# recipes/views.py

from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
from . import models

def index(request):
  return render(request, 'recipes/index.html')

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})

def recipes(request):
   recipes = Recipe.objects.all()
   return render(request, 'recipes/recipes.html')


def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def view_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/view_recipe.html', {'recipe': recipe})

def home(request):
  recipes = models.Recipe.objects.all()
  context = {
    'recipes': recipes
  }
  return render(request, 'recipes/home.html', context)

def about(request):
  return render(request, 'recipes/about.html', {'title': 'about page'})

def base(request):
   return render(request, 'recipes/base.html')


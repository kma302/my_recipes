# recipes/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('base/', views.base, name='base'),
    path('', views.index, name ='index'),
    path('view/<int:recipe_id>/', views.view_recipe, name='view_recipe'),
] 
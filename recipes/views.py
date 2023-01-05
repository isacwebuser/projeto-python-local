from django.http import HttpResponse
from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Recipe

# Create your views here.


def my_home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'recipe_detail': True,
    })


def category(request, category_id):
    category = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': category,
        'title': f' | Category - {category.first().category.name}'
    })

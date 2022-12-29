from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def my_home(request):
    return render(request, 'recipes/pages/home.html', context={
        'nome': 'Isac Souza',
        })
        
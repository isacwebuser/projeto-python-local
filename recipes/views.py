from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_home(request):
    return render(request, 'templates/home.html', context={
        'nome': 'Isac Souza',
        })


def sobre(request):
    return HttpResponse('Sobre')
    

def contato(request):
    return HttpResponse('Contato')

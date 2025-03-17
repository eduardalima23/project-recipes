from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('Home')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Eduarda Lima',
    })


def sobre(request):
    return render(request, 'recipes/contato.html')


def contato(request):
    return HttpResponse('Contato')

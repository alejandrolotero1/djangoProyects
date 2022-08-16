# from django.http import HttpResponse
from django.shortcuts import render


def Index(request):
    return render(request, 'Principal.html')

def Noticias(request):
    return render(request, 'Noticias.html')

# Create your views here.

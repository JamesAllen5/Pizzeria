from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}

    return render(request,'MainApp/pizzas.html', context)
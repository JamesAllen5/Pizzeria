from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def pizzas(request):
    pizzas = Pizza.objects.all()

    context = {'pizzas':pizzas}

    return render(request, 'MainApp/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    topping = pizza.topping_set.all()

    context = {'pizza':pizza,'toppings':topping}

    return render(request, 'MainApp/pizza.html', context)



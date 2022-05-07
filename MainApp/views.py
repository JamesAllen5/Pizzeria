from django.shortcuts import render, redirect
from .models import Pizza, Topping, Comment
from .forms import  PizzaForm, ToppingForm, CommentForm

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
    picture = Pizza.picture
    comment = pizza.comment_set.order_by('-date_added')

    context = {'pizza':pizza,'toppings':topping, 'picture': picture, 'comments':comment}

    return render(request, 'MainApp/pizza.html', context)


def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form=CommentForm()
    else:
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            return redirect('MainApp:pizza',pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}

    return render(request, 'MainApp/comment.html', context)
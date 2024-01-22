from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import ShoppingList
import requests
import os

# Variables

api = os.environ['APIKEY']
random_10 = '/randomselection.php'
random = '/random.php'
popular_10 = '/popular.php'
latest = '/latest.php'
search = '/search.php?s=' #{Drink Name}
letter_search = '/search.php?f=' #{Drink first letter}
ingredient_search = '/search.php?i=' #{ingredient name}
drink_id = '/lookup.php?i=' #{Lookup by ID for SHOW page}
ingredient_id = '/lookup.php?iid=' #{Lookup ingredient by ID}

# Create views here.

def home(request):
    url = f"https://www.thecocktaildb.com/api/json/v2/{api}{popular_10}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()

    drinks = filter(lambda drink: drink, response['drinks'])
    return render(request, 'home.html', {'response': response, 'api': api, 'drink_id': drink_id, 'drinks': drinks})


def random_index(request):
    url = f"https://www.thecocktaildb.com/api/json/v2/{api}{random_10}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    drinks = filter(lambda drink: drink, response['drinks'])
    return render(request, 'random.html', {'response': response, 'api': api, 'drink_id': drink_id, 'drinks': drinks})


def about(request):
    return render(request, 'about.html', )


def drinks_index(request):
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    drinks = response.json()['drinks']
    return render(request, 'index.html', {'drinks':drinks})


def show_page(request, id_drink):
    url = f'https://www.thecocktaildb.com/api/json/v2/{api}{drink_id}{id_drink}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
<<<<<<< HEAD
    ## drinks = response.json()['drinks']
    return render(request, 'show.html', {'response': response, 'api': api })
=======
    response = response.json()
>>>>>>> e3bd0da5124b9c77be7a9219d2a980bb65487159

    return render(request, 'show.html', {'response': response, 'api': api})


def registration(request, user):
    pass

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home.html') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user/login.html') 

def add_to_shopping_list(request, ingredient_name):
    user = request.user
    ShoppingList.objects.create(user=user, ingredient_name=ingredient_name)
    return render(request, 'show.html')


def ShoppingList(request):
    return render(request, 'ShoppingList.html')


def delete_from_shopping_list(request, ingredient_id):
    shopping_list_entry =  get_object_or_404(ShoppingList, ingredient_id=ingredient_id, user=request.user)
    shopping_list_entry.delete()
    return redirect(request, 'ShoppingList.html')
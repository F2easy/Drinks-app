from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Shopping_list
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
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
    ing_arr = []
    url = f'https://www.thecocktaildb.com/api/json/v2/{api}{drink_id}{id_drink}'
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    drinks = filter(lambda drink: drink, response['drinks'])
    return render(request, 'show.html', {'response': response, 'api': api, 'drinks': drinks})



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

# Shopping list Views


# we want to do this without displaying a form ask Tylus (fieldset)
# add to Shopping List
def add_to_shopping_list(request, drink_id):
    drink_id = drink_id
    model = Shopping_list
    user = request.user
    Shopping_list.objects.create({'user': user , 'drink_id': drink_id})
    return render(request, 'shopping_list.html')

# ShoppingList Details
class ShoppingList(ListView):
    model = Shopping_list
    template_name = 'shopping_list.html'

# Delete from ShoppinList
class delete_from_shopping_list(DeleteView):
    model = Shopping_list
    success_urls = '/shopping_list'

## class ListDetail(DetailView)
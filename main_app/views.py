from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
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
api = os.environ['APIKEY']

def home(request):
    url = f"https://www.thecocktaildb.com/api/json/v2/{api}/{random_10}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()
    print(f'This is response{response}')
    drink = response.get('drinks')[0]['strDrink']
    # drink.json
    return render(request, 'home.html', {'response': response, 'api': api, 'drink_id': drink_id, 'drink': drink})



def about(request):
    return render(request, 'about.html', )


def drinks_index(request):
    api_key = os.environ['APIKEY']
    url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, data=payload)
    drinks = response.json()['drinks']

    return render(request, 'index.html', {'drinks':drinks})

def show_page(request, idDrink):

    url = f'https://www.thecocktaildb.com/api/json/v2/{api}{drink_id}/'#drinkID
    return(render(request, 'show.html'))

    

def add_to_shopping_list(request, ingredient_name):
    user = request.user
    ShoppingList.objects.create(user=user, ingredient_name=ingredient_name)
    return render(request, 'show.html')

#If link in the show page or the nav bar, user should see all the ingrdients that have been added to the list 
def ShoppingList(request):
    return render(request, 'ShoppingList.html')

def delete_from_shopping_list(request, ingredient_id):
    shopping_list_entry =  get_object_or_404(ShoppingList, ingredient_id=ingredient_id, user=request.user)
    shopping_list_entry.delete()
    return redirect(request, 'ShoppingList.html')
    



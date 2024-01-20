from django.shortcuts import render
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
    url = f"https://www.thecocktaildb.com/api/json/v2/{api}/{random_10}"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json
    
    return render(request, 'home.html', {'response': response})


def about(request):
    return render(request, 'about.html')


def drinks_index(request):
    return render(request, 'index.html')

def show_page(request):
    return(render(request, 'show.html'))
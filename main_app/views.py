from django.shortcuts import render
import requests

# Create views here.

def home(request):
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
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


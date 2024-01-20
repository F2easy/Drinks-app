from django.shortcuts import render
import requests


def home(request):
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json
    
    return render(request, 'home.html', {'response': response})


def about(request):
    return render(request, 'about.html')
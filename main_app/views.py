from django.shortcuts import render
import requests

url = "www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


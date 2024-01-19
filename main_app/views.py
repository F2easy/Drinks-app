from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def drinks_index(request):
    return render(request, 'index.html')

def show_page(request):
    return(render(request, 'show.html'))

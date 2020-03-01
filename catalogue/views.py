from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'catalogue/home.html', context={})

def books(request):
    return render(request, 'catalogue/books.html', context={})

def recipes(request):
    return render(request, 'catalogue/recipes.html', context={})
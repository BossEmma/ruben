from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'detail.html')


def search(request):
    return render(request, 'search.html')


def cart(request):
    return render(request, 'cart.html')


def phones(request):
    return render(request, 'category.html')
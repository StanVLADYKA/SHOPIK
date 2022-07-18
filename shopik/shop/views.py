from django.shortcuts import render
from .models import Category, Products

def home(request):
    context = {
        "categories": Category.objects.all(),
        "products":Products.objects.all(),
    }
    return render(request, "shopik/home.html", context)
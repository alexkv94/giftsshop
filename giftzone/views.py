from django.shortcuts import render
from store.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()[0:5]

    return render(request, 'giftzone/home.html', {
        'products': products
    })

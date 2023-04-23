from django.shortcuts import render, get_object_or_404
from .models import Product

def product_details(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_details.html', {
        'product': product
    })

def category_extra(request, slug):
    return render(request, 'store/categories.html')

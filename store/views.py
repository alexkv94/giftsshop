from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_details(request, category_slug, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_details.html', {
        'product': product
    })

def category_extra(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'store/category_extra.html', {
        'category': category,
        'products': products
    })

def search(request):
    search_query = request.GET.get('search_query', '')
    products = Product.objects.filter(title__icontains=search_query)
    return render(request, 'store/search.html', {
        'search_query': search_query,
        'products': products
    })

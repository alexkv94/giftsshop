from django.shortcuts import render
from .models import Categories

# Create your views here.

def index(request):
    return render(request, 'giftzone/index.html')

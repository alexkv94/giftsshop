from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Userprofile


def user_details(request, primary_key):
    user = User.objects.get(primary_key=primary_key)
    return render(request, 'userprofile/user_details.html',
                  {
                      'user': user
                  })

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_profile = Userprofile.objects.create(user=user)

            return redirect('home')

    else:
        form = UserCreationForm()

    return render(request, 'users/create_user.html', {
        'form': form
    })

def accountinfo(request):
    return render(request,'users/account.html')

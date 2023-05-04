from django.urls import path
from django.contrib.auth import views as views_in_auth
from . import views

urlpatterns = [
    path('users/<int:primary_key/', views.user_details, name='user_details'),
    path('create_user/', views.create_user, name='user_signup'),
    path('account/', views.accountinfo, name='accountinfo'),
    path('logout/', views_in_auth.LogoutView.as_view(), name='logout'),
    path('login/', views_in_auth.LoginView.as_view(template_name='users/login.html')),

]
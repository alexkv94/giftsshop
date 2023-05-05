from django.urls import path
from . import views

urlpatterns = [
    path("add-to-cart/<int:product_id>/", views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('search/', views.search, name='search'),
    path("<slug:category_slug>/<slug:slug>/", views.product_details, name='product_details'),
    path("<slug:slug>/", views.category_extra, name='category_extra'),

]

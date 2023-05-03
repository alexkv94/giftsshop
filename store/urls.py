from django.urls import path
from . import views

urlpatterns = [
    path("<slug:category_slug>/<slug:slug>/", views.product_details, name='product_details'),
    path("<slug:slug>/", views.category_extra, name='category_extra'),
]
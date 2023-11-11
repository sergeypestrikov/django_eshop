from django.urls import path
from .views import products, product

urlpatterns = [
    path('', products, name='products'),
    path('product/<int:id>/', product, name='product'),
    path('category/<int:pk>/', products, name='category'),
]
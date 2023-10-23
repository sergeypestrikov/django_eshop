from django.urls import path
from .views import products, product

urlpatterns = [
    path('', products, name='products'),
    path('<int:id>/', product, name='product'),
]
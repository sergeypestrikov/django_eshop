from django.urls import path
from .views import products, product

# app_name = 'product_app'

urlpatterns = [
    path('', products, name='products'),
    path('product/<int:id>/', product, name='product'),
    path('category/<int:pk>/', products, name='category'),
    path('<int:pk>/', product, name='detail'),
    path('category/page/<int:page>/', products, name='page'),
]
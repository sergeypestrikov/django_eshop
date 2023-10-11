from django.shortcuts import render


# Контроллер продуктовой страницы
def products(request):
    return render(request, 'product_app/products.html')
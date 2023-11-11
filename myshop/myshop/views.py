from django.shortcuts import render


# Контроллер главной страницы
from basket_app.models import Basket
from product_app.models import Product


def index(request):
    products = Product.objects.all()[:3]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'главная',
        'products': products,
        'basket': basket,
    }
    return render(request, 'myshop/index.html', context=context)


# Контроллер страницы о нас
def about(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'о нас'
    }
    return render(request, 'myshop/about.html', context=context)


# Контроллер страницы с контактами
def contacts(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': 'контакты'
    }
    return render(request, 'myshop/contact.html', context=context)
from django.shortcuts import render


# Контроллер главной страницы
from product_app.models import Product


def index(request):
    products = Product.objects.all()[:3]

    context = {
        'title': 'главная',
        'products': products,
    }
    return render(request, 'myshop/index.html', context=context)


# Контроллер страницы о нас
def about(request):
    context = {
        'title': 'о нас'
    }
    return render(request, 'myshop/about.html', context=context)


# Контроллер страницы с контактами
def contacts(request):
    context = {
        'title': 'контакты'
    }
    return render(request, 'myshop/contact.html', context=context)
import random

from django.shortcuts import render, get_object_or_404

from basket_app.models import Basket
from product_app.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


# Контроллер горячих предложений? рандомно выводимых на странице
def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


# Получение похожего продукта
def get_same_product(hot_product):
    same_product = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk).order_by('price')
    return same_product


# Контроллер продуктовой страницы
def products(request, pk=None, page=1):
    title = 'каталог'
    catalog = Product.objects.all()[:]
    links_menu = ProductCategory.objects.all()

    basket = get_basket(request.user)

    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }
        return render(request, 'product_app/product_list.html', context)

    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)

    # paginator = Paginator(products, 2)
    # try:
    #     products_paginator = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paginator = paginator.page(1)
    # except EmptyPage:
    #     products_paginator = paginator.page(paginator.num_pages)

    context = {
        'title': title,
        'object': catalog,
        # 'product': products_paginator,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_product': same_product,
        'basket': basket,
    }
    return render(request, 'product_app/products.html', context=context)


# Контроллер страницы конкретного продукта
def product(request, pk):
    title = 'детальное описание'
    link_menu = ProductCategory.objects.all()
    product = get_object_or_404(Product, pk=pk)
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)

    context = {
        'title': title,
        'link_menu': link_menu,
        'product': product,
        'same_product': same_product,
        'basket': basket,
    }

    return render(request, 'product_app/product.html', context=context)
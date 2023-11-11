from django.shortcuts import render, get_object_or_404

from basket_app.models import Basket
from product_app.models import Product, ProductCategory


# Контроллер страницы конкретного продукта
def product(request, id):
    context = {
        'title': 'страница товара',
        'object': Product.objects.get(pk=id)
    }
    print(id)
    return render(request, 'product_app/product.html', context=context)


# Контроллер продуктовой страницы
def products(request, pk=None):
    title = 'каталог'
    catalog = Product.objects.all()[:]
    links_menu = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

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

    same_product = Product.objects.all()[2:4]

    context = {
        'title': title,
        'object': catalog,
        'links_menu': links_menu,
        'same_product': same_product,
        'basket': basket,
    }
    return render(request, 'product_app/products.html', context=context)
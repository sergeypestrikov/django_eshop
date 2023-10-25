from django.shortcuts import render
from product_app.models import Product


# Контроллер страницы конкретного продукта
def product(request, id):
    context = {
        'title': 'страница товара',
        'object': Product.objects.get(pk=id)
    }
    print(id)
    return render(request, 'product_app/product.html', context=context)


# Контроллер продуктовой страницы
def products(request):
    catalog = Product.objects.all()[:]

    context = {
        'title': 'каталог',
        'object': catalog,
    }
    return render(request, 'product_app/products.html', context=context)
    # context = {
    #     'title': 'каталог',
    #     'object': Product.objects.get(id=3)
    # }
    # return render(request, 'product_app/products.html', context=context)
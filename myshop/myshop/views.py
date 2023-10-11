from django.shortcuts import render


# Контроллер главной страницы
def index(request):
    context = render(request, 'myshop/index.html')
    return context


# Контроллер страницы о нас
def about(request):
    return render(request, 'myshop/about.html')


# Контроллер страницы с контактами
def contacts(request):
    return render(request, 'myshop/contact.html')
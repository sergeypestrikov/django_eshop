from django.urls import path
import basket_app.views as basket_app

app_name = 'basket_app'

urlpatterns = [
    path('', basket_app.basket, name='view'),
    path('add/<int:pk>/', basket_app.basket_add, name='add'),
    path('remove/<int:pk>/', basket_app.basket_remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket_app.basket_edit, name='edit'),
]
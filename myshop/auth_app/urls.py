from django.urls import path
import auth_app.views as auth_app

app_name = 'auth_app'

urlpatterns = [
    path('register/', auth_app.register, name='register'),
    path('edit/', auth_app.edit, name='edit'),
    path('login/', auth_app.login, name='login'),
    path('logout/', auth_app.logout, name='logout'),
]
from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Pagina principală cu lista de laptopuri
    path('produs/<str:serielaptop>/', views.product_detail, name='product_detail'),  # Detalii despre un laptop
    path('cart/', views.cart, name='cart'),  # Coșul de cumpărături (temporar simplu)
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
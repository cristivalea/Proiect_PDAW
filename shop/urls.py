from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Pagina principală cu lista de laptopuri
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/adaugare-laptop/', views.adaugare_laptop, name='adaugare_laptop'),
]
from django.contrib import admin
from django.urls import path, include
from shop import views


urlpatterns = [
    path('', views.index, name='/'),
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('', include('shop.urls')),
]
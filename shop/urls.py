from django.urls import path
from shop import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Pagina principală cu lista de laptopuri
    path('login/', views.login_view, name='login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('register/', views.register, name='register'),

    path('admin-dashboard/adaugare_laptop/', views.adaugare_laptop, name='adaugare_laptop'),
    path('admin-dashboard/cautare_laptop/', views.cautare_laptop, name='cautare_laptop'),
    path('delete-laptop/', views.delete_laptop, name='delete_laptop'),
    path('edit-laptop/<str:serielaptop>/', views.edit_laptop, name='edit_laptop'),

    path('admin-dashboard/adauga_tableta/', views.adauga_tableta, name='adauga_tableta'),
    path('admin-dashboard/cautare_tableta/', views.cautare_tableta, name='cautare_tableta'),
    path('edit_tableta/<str:serietableta>/', views.edit_tableta, name='edit_tableta'),
    path('delete_tableta/', views.delete_tableta, name='delete_tableta'),

    path('admin-dashboard/adaugare_telefoan/', views.adaugare_telefon, name='adaugare_telefon'),
    path('admin-dashboard/cautare_telefon/', views.cautare_telefon, name='cautare_telefon'),
    path('edit_telefon/<str:serie>/', views.editare_telefon, name='edit_telefon'),
    path('delete_telefon/', views.delete_telefon, name='delete_telefon'),

    path('admin-dashboard/cautare_utilizatori', views.cauta_utilizatori, name='cautare_utilizatori'),
    path('admin-dashboard/sterge_utilizator/<int:user_id>/', views.sterge_utilizator, name='sterge_utilizator'),
    path('admin-dashboard/editare_utilizator/<int:user_id>/', views.editare_utilizator, name='editare_utilizator'),

    path('', views.index, name='index'),
    path('login/', views.custom_login, name='login'),
]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # Include URL-urile aplicației tale (de exemplu, 'shop.urls')
    path('', include('shop.urls')),  # presupun că ai un fișier shop/urls.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

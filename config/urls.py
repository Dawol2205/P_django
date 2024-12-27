# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_products(request):
    return redirect('products:index')

urlpatterns = [
    path('', redirect_to_products, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('board/', include('board.urls')),  # 이 줄을 추가
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views import home_page

urlpatterns = [
    path('', home_page),
    path('', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('api/', include("products.api.api_urls")),
]

if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

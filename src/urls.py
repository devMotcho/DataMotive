from django.contrib import admin
from django.urls import path, include


from django.conf import settings
from django.conf.urls.static import static
from .settings import IS_PRODUCTION

urlpatterns = [
    path('', include('dashboard.urls')),
    path('authentic/', include('authentic.urls')),
    path('product/', include('product.urls')),
    path('stock/', include('stock.urls')),
    path('partners/', include('partners.urls')),
    path('transactions/', include('transactions.urls'))
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)


if not IS_PRODUCTION:
    urlpatterns += [
        path('gest/admin/', admin.site.urls),
    ]
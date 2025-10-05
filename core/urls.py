from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_apps.carpena.urls', namespace='carpena')),
    path('accounts/', include('my_apps.accounts.urls', namespace='accounts')),
    path('money/', include('my_apps.my_money.urls', namespace='my_money')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
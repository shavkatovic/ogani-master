from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users', include('users.urls')),
                  path('', include('product.urls'))
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

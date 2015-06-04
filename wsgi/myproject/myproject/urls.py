from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ezine.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

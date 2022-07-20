from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/gallery/', include('gallery.urls')),
    path('api/schedule/', include('schedule.urls')),
    path('api/clergy/', include('clergy.urls')),
    path('api/donation/', include('donation.urls')),
    path('api/contacts/', include('contact.urls'))

]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

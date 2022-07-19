from django.urls import path
from .views import LCGalleryAlbumView, RUDGalleryAlbumView, RUDGalleryAlbumImage

urlpatterns = [
    path('album', LCGalleryAlbumView.as_view(), name='list-create'),
    path('album/<int:pk>', RUDGalleryAlbumView.as_view(), name='rud-album'),
    path('album/image/<int:pk>', RUDGalleryAlbumImage.as_view(), name='rud-image')
]

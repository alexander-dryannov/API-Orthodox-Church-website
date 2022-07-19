from django.urls import path
from .views import LCGalleryAlbumView, RUDGalleryAlbumView, DGalleryAlbumImage

urlpatterns = [
    path('album', LCGalleryAlbumView.as_view(), name='list-create'),
    path('album/<int:pk>', RUDGalleryAlbumView.as_view(), name='retrieve-update-delete'),
    path('album/image/<int:pk>', DGalleryAlbumImage.as_view(), name='delete')
]

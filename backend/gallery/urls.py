from django.urls import path
from .views import LCAlbumView, RUDAlbumView, LCImagesView, RUDImageView


urlpatterns = [
    path('albums', LCAlbumView.as_view(), name='list-album'),
    path('album/<int:pk>', RUDAlbumView.as_view(), name='retrieve'),
    path('images', LCImagesView.as_view(), name='list-image'),
    path('image/<int:pk>', RUDImageView.as_view(), name='retrieve-image')
]

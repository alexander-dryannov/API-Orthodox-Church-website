from django.urls import path
from .views import GalleryAlbumListView, GalleryAlbumCreateView

urlpatterns = [
    path('album_list', GalleryAlbumListView.as_view(), name='list-view'),
    path('create_album', GalleryAlbumCreateView.as_view(), name ='create-view')
]


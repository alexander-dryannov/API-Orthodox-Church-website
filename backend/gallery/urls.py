from django.urls import path
from .views import GalleryAlbumRetrieveUpdateDestroyView, GalleryAlbumListCreateView

urlpatterns = [
    path('album', GalleryAlbumListCreateView.as_view(), name='list-create'),
    path('album/<int:pk>', GalleryAlbumRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete'),
]

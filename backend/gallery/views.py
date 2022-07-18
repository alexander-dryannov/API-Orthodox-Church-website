from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from .models import GalleryAlbum
from .serializers import GalleryAlbumSerializer


class GalleryAlbumListView(ListAPIView):
    queryset = GalleryAlbum
    serializer_class = GalleryAlbumSerializer
    

class GalleryAlbumCreateView(CreateAPIView):
    serializer_class = GalleryAlbumSerializer
    parser_classes = (MultiPartParser, FormParser)

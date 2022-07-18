from rest_framework import status
from .handlers import convert_image
from django.http import JsonResponse
from .models import GalleryAlbum, GalleryAlbumImage
from .serializers import GalleryAlbumSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class GalleryAlbumListCreateView(ListCreateAPIView):
    queryset = GalleryAlbum.objects.all()
    serializer_class = GalleryAlbumSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            images = request.data.pop('images')
            cover, _, _ = convert_image(request.data['cover'])
            request.data['cover'] = cover
            album_obj = GalleryAlbum.objects.create(**request.data.dict())
            for image in images:
                image, height, width = convert_image(image, field_name=image)
                GalleryAlbumImage.objects.create(album=album_obj, image=image, width=width, height=height)
            return JsonResponse({'status_code': status.HTTP_201_CREATED})
        finally:
            GalleryAlbum.objects.create(**request.data.dict())
            return JsonResponse({'status_code': status.HTTP_201_CREATED})


class GalleryAlbumRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = GalleryAlbum.objects.all()
    serializer_class = GalleryAlbumSerializer

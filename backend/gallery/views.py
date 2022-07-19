from email.mime import image
from .handlers import convert_image
from django.http import JsonResponse
from .models import GalleryAlbum, GalleryAlbumImage
from .serializers import GalleryAlbumSerializer, GalleryAlbumImageSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView


class LCGalleryAlbumView(ListCreateAPIView):
    queryset = GalleryAlbum.objects.all()
    serializer_class = GalleryAlbumSerializer
    
    def post(self, request, *args, **kwargs):
        if request.data.get('images'):
            images = request.data.pop('images')
            cover, _, _ = convert_image(request.data['cover'])
            request.data['cover'] = cover
            self.create(request, *args, **kwargs)
            for image in images:
                image, height, width = convert_image(image, field_name=image)
                GalleryAlbumImage.objects.create(album=self.queryset.last(), image=image, width=width, height=height)
            return JsonResponse({'message': 'Альбом создан.'}, json_dumps_params={'ensure_ascii': False})
        else:
            super().create(request, *args, **kwargs)
            return JsonResponse({'message': 'Создан пустой альбом.'}, json_dumps_params={'ensure_ascii': False})


class RUDGalleryAlbumView(RetrieveUpdateDestroyAPIView):
    queryset = GalleryAlbum.objects.all()
    serializer_class = GalleryAlbumSerializer
    
    def patch(self, request, *args, **kwargs):
        if request.data.get('images'):
            images = request.data.pop('images')
            for image in images:
                image, height, width = convert_image(image, field_name='image')
                GalleryAlbumImage.objects.create(album=self.queryset.last(), image=image, width=width, height=height)
        return super().patch(request, *args, **kwargs)


class RUDGalleryAlbumImage(RetrieveUpdateDestroyAPIView):
    queryset = GalleryAlbumImage.objects.all()
    serializer_class = GalleryAlbumImageSerializer
    
    def patch(self, request, *args, **kwargs):
        if request.data.get('image'):
            image, height, width = convert_image(request.data.get('image'), field_name='image')
            request.data['image'] = image
            request.data['width'] = width
            request.data['height'] = height
        return super().patch(request, *args, **kwargs)

from .models import Album, Image
from rest_framework import generics
from django.http import JsonResponse
from .serializers import ImageSerializer, ImageGetByIdSerializer, AlbumSerializer, AlbumGetByIdSerializer


class LCAlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class RUDAlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumGetByIdSerializer


class LCImagesView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        dump = {'images': []}
        album_id = int(request.data.pop('pk')[0])
        if request.data.get('images'):
            items = request.data.pop('images')
            request.data['album'] = album_id
            for item in items:
                request.data['src'] = item
                image_dict = self.create(request, *args, **kwargs)
                dump['data'].append(image_dict.data)
        return JsonResponse(dump)


class RUDImageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageGetByIdSerializer

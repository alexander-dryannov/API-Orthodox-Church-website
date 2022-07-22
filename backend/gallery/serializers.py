from .models import Album, AlbumImage
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ['id', 'album', 'src', 'width', 'height', 'origin_width', 'origin_height']


class ImageGetByIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlbumImage
        fields = ['id', 'src']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'cover', 'description']


class AlbumGetByIdSerializer(serializers.ModelSerializer):
    images = ImageSerializer(source='album', many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'images']
        depth = 1

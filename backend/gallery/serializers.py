from rest_framework import serializers
from .models import GalleryAlbumImage, GalleryAlbum


class GalleryAlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbumImage
        fields = ['id', 'image', 'width', 'height',
                  'is_visible', 'created_at', 'updated_at']


class GalleryAlbumSerializer(serializers.ModelSerializer):
    images = GalleryAlbumImageSerializer(source='album', many=True,
                                         required=False, allow_null=False)

    class Meta:
        model = GalleryAlbum
        fields = ['id', 'title', 'cover', 'slug',
                  'is_visible', 'created_at', 'updated_at', 'images']
        depth = 1

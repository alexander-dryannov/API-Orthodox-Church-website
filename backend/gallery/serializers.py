from pyexpat import model
from rest_framework import serializers
from .models import GalleryAlbumImage, GalleryAlbum


class GalleryAlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbumImage
        fields = ['album', 'id', 'image', 'width', 'height', 'visible', 'created_at', 'updated_at']


class GalleryAlbumNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbumImage
        fields = ['id', 'image', 'width', 'height', 'visible', 'created_at', 'updated_at']
        

class GalleryAlbumCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField())
    
    class Meta:
        model = GalleryAlbum
        fields = ['id', 'title', 'cover', 'visible', 'images']


class GalleryAlbumSerializer(serializers.ModelSerializer):
    images = GalleryAlbumNestedSerializer(source='album', many=True)
    class Meta:
        model = GalleryAlbum
        fields = ['id', 'title', 'cover', 'slug', 'visible', 'created_at', 'updated_at', 'images']
        depth = 1

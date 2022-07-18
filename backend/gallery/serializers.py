from .handlers import convert_image
from rest_framework import serializers
from .models import GalleryAlbumImage, GalleryAlbum


class GalleryAlbumImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbumImage
        fields = ['album', 'image', 'width', 'height' 'visible']
        

class GalleryAlbumSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField())
    
    class Meta:
        model = GalleryAlbum
        fields = ['id', 'title', 'cover', 'visible', 'images']
        depth = 1
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        cover, _, _ = convert_image(image=validated_data['cover'], field_name='cover')
        validated_data['cover'] = cover
        title = validated_data['title']
        visible = validated_data['visible']
        album = GalleryAlbum.objects.create(title=title, cover=cover, visible=visible)
        for image in images:
            image, height, width = convert_image(image, field_name=image)
            GalleryAlbumImage.objects.create(album=album, image=image, width=width, height=height)
        return album
    
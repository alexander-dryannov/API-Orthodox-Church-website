import uuid
from pathlib import Path
from django.db import models
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete


class GalleryAlbum(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(blank=True, upload_to='gallery_album')
    slug = models.SlugField(unique=True, max_length=42, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse('album_details', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4().hex
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class GalleryAlbumImage(models.Model):
    album = models.ForeignKey(GalleryAlbum, on_delete=models.CASCADE, related_name='album')
    image = models.ImageField(upload_to='gallery_album_images', height_field='height', width_field='width')
    height = models.PositiveIntegerField(blank=True, default=0)
    width = models.PositiveIntegerField(blank=True, default=0)
    slug = models.SlugField(unique=True, max_length=42, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid.uuid4().hex
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.slug
    
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(post_delete, sender=GalleryAlbumImage)
def delete_file(sender, instance, *args, **kwargs):
    if instance.image:
        Path.unlink(Path(instance.image.path))


@receiver(post_delete, sender=GalleryAlbum)
def delete_file(sender, instance, *args, **kwargs):
    if instance.cover:
        Path.unlink(Path(instance.cover.path))

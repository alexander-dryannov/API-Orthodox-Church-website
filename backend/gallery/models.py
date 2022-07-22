from uuid import uuid4
from pathlib import Path
from django.db import models
from .handlers import converter
from django.dispatch import receiver
from django.db.models.signals import post_delete


class BaseModel(models.Model):
    slug = models.SlugField(unique=True, max_length=42, blank=True)
    created_at = models.DateTimeField('Дата и время создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата и время обновления', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class Album(BaseModel):
    title = models.CharField('Название', max_length=100)
    cover = models.ImageField('Обложка', blank=True, upload_to='album_covers')
    description = models.TextField('Описание', blank=True)

    def save(self, *args, **kwargs):
        if self.cover:
            cover, *_ = converter(self.cover)
            self.cover = cover
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class AlbumImage(BaseModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
    src = models.ImageField('Изображение', upload_to='album_images')
    origin_height = models.PositiveIntegerField('Оригинальная высота', blank=True, default=0)
    origin_width = models.PositiveIntegerField('Оригинальная ширина', blank=True, default=0)
    height = models.PositiveIntegerField('Относительная высота', blank=True, default=0)
    width = models.PositiveIntegerField('Относительная ширина', blank=True, default=0)

    def save(self, *args, **kwargs):
        if self.src:
            src, width, height, origin_width, origin_height = converter(self.src)
            self.src = src
            self.width = width
            self.height = height
            self.origin_width = origin_width
            self.origin_height = origin_height
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


@receiver(post_delete, sender=AlbumImage)
def delete_file(sender, instance, *args, **kwargs):
    if instance.src:
        Path.unlink(Path(instance.src.path))


@receiver(post_delete, sender=Album)
def delete_file(sender, instance, *args, **kwargs):
    if instance.cover:
        Path.unlink(Path(instance.cover.path))

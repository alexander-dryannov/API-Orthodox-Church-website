from uuid import uuid4
from pathlib import Path
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Post(models.Model):
    title = models.CharField('Название', max_length=100)
    cover = models.ImageField('Обложка', upload_to='cover_post', blank=True)
    body = models.TextField('Текст')
    slug = models.SlugField(max_length=42, blank=True, unique=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


@receiver(post_delete, sender=Post)
def delete_file(sender, instance, *args, **kwargs):
    if instance.cover:
        Path.unlink(Path(instance.cover.path))

from uuid import uuid4
from pathlib import Path
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete


class Cleric(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=42, blank=True, unique=True)
    data = models.JSONField()
    photo = models.ImageField(upload_to='cleric_photo', blank=True)
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клирик'
        verbose_name_plural = 'Клирики'


@receiver(post_delete, sender=Cleric)
def delete_file(sender, instance, *args, **kwargs):
    if instance.photo:
        Path.unlink(Path(instance.photo.path))

from uuid import uuid4
from django.db import models
from django.urls import reverse


class Schedule(models.Model):
    title = models.CharField(max_length=99)
    data = models.JSONField()
    slug = models.SlugField(max_length=42, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'

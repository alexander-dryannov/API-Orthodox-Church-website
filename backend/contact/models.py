from uuid import uuid4
from django.db import models


class Contact(models.Model):
    title = models.CharField('Название', max_length=100)
    address = models.TextField('Адрес')
    mobile_phone = models.CharField('Мобильный телефон', max_length=20)
    landline_phone = models.CharField('Стационарный телефон', max_length=20)
    email = models.EmailField('Электронная почта')
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
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

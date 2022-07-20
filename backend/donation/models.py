from uuid import uuid4
from django.db import models


class Donation(models.Model):
    description = models.TextField('Описание')
    inn = models.CharField('ИНН', max_length=20)
    kpp = models.CharField('КПП', max_length=20)
    ogrn = models.CharField('ОГРН', max_length=20)
    okpo = models.CharField('ОКПО', max_length=20)
    payment_account = models.CharField('Расчетный счет', max_length=20)
    bank = models.TextField('Банк')
    bic = models.CharField('БИК', max_length=20)
    correspondent_account = models.CharField('Корр. счет', max_length=20)
    legal_address = models.TextField('Юридический адрес')
    telephone = models.CharField('Телефон', max_length=20)
    abbot = models.CharField('Настоятель', max_length=100)
    slug = models.SlugField(max_length=42, blank=True, unique=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    is_visible = models.BooleanField('Видимость', default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = uuid4().hex
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.abbot

    class Meta:
        verbose_name = 'Пожертвование'
        verbose_name_plural = 'Пожертвования'

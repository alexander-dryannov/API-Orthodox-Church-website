# Generated by Django 4.0.6 on 2022-07-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryalbumimage',
            name='image_height',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='galleryalbumimage',
            name='image_width',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]

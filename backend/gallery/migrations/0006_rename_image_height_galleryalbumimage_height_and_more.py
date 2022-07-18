# Generated by Django 4.0.6 on 2022-07-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_galleryalbumimage_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='galleryalbumimage',
            old_name='image_height',
            new_name='height',
        ),
        migrations.RenameField(
            model_name='galleryalbumimage',
            old_name='image_width',
            new_name='width',
        ),
        migrations.AddField(
            model_name='galleryalbum',
            name='cover',
            field=models.ImageField(blank=True, upload_to='gallery_album'),
        ),
        migrations.AlterField(
            model_name='galleryalbumimage',
            name='image',
            field=models.ImageField(height_field='height', upload_to='gallery_album_images', width_field='width'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clergy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleric',
            name='slug',
            field=models.SlugField(blank=True, max_length=42, unique=True),
        ),
    ]

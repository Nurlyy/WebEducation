# Generated by Django 4.0.4 on 2022-05-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_theme_file_field_alter_theme_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='image',
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-22 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='file_field',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
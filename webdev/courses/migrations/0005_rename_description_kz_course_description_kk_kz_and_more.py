# Generated by Django 4.0.4 on 2022-05-24 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_description_kz_course_description_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='description_kz',
            new_name='description_kk_KZ',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='title_kz',
            new_name='title_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='first_text_kz',
            new_name='first_text_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='first_title_kz',
            new_name='first_title_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='second_text_kz',
            new_name='second_text_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='second_title_kz',
            new_name='second_title_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='third_text_kz',
            new_name='third_text_kk_KZ',
        ),
        migrations.RenameField(
            model_name='theme',
            old_name='third_title_kz',
            new_name='third_title_kk_KZ',
        ),
    ]

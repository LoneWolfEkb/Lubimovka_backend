# Generated by Django 3.2.12 on 2022-04-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_delete_other_play'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationapplicationfestival',
            name='url_file_in_storage',
            field=models.URLField(blank=True, max_length=512, verbose_name='Ссылка для скачивания файла с Диска'),
        ),
    ]
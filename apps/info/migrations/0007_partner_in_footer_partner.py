# Generated by Django 3.2.9 on 2021-12-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20211115_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='in_footer_partner',
            field=models.BooleanField(default=False, help_text='Поставьте галочку, чтобы показать логотип партнёра внизу страницы', verbose_name='Отображение внизу страницы'),
        ),
    ]
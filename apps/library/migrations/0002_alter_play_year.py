# Generated by Django 3.2.11 on 2022-02-01 19:12

import apps.library.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[apps.library.validators.year_validator], verbose_name='Год написания пьесы'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-10-12 19:54

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_person_image'),
        ('afisha', '0004_auto_20211007_1713'),
        ('library', '0002_auto_20211004_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationApplicationFestival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='День рождения')),
                ('city', models.CharField(max_length=50, verbose_name='Город проживания')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=100, verbose_name='Электронная почта')),
                ('title', models.CharField(max_length=200, verbose_name='Название пьесы')),
                ('year', models.CharField(max_length=4, verbose_name='Год написания')),
                ('file_link', models.URLField(verbose_name='Ссылка на файл')),
                ('status', models.BooleanField(verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заявление на участие',
                'verbose_name_plural': 'Заявления на участие',
            },
        ),
        migrations.AlterModelOptions(
            name='performance',
            options={'ordering': ('-created',), 'verbose_name': 'Спектакль', 'verbose_name_plural': 'Спектакли'},
        ),
        migrations.AddField(
            model_name='performance',
            name='age_limit',
            field=models.CharField(default='0+', max_length=3, verbose_name='Возрастное ограничение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='bottom_image',
            field=models.ImageField(default=None, upload_to='performances/', verbose_name='Изображение внизу страницы'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='event',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='performances', to='afisha.commonevent', verbose_name='Базовое событие'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='full_description',
            field=models.TextField(default=None, verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='images_in_block',
            field=models.ManyToManyField(blank=True, null=True, to='core.Image', verbose_name='Фотографии спектакля в блоке фотографий'),
        ),
        migrations.AddField(
            model_name='performance',
            name='main_image',
            field=models.ImageField(default=None, upload_to='performances/', verbose_name='Главное изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='play',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='performances', to='library.play', verbose_name='Пьеса'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='short_description',
            field=models.TextField(default=None, max_length=500, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='video',
            field=models.FileField(default=None, upload_to='performances/', verbose_name='Видео'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='performance',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название спектакля'),
        ),
    ]
# Generated by Django 3.2.7 on 2021-10-17 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_added_model_performance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterclass',
            name='director',
        ),
        migrations.RemoveField(
            model_name='masterclass',
            name='dramatist',
        ),
    ]

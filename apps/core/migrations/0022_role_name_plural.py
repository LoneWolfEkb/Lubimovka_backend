# Generated by Django 3.2.10 on 2021-12-30 12:23

from django.db import migrations, models

def set_name_plural(apps, schema_editor):
    Role = apps.get_model("core", "Role")
    for role in Role.objects.all():
        if len(role.name_plural) == 0:
            role.name_plural = role.name + "'s"
            role.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_alter_setting_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='name_plural',
            field=models.CharField(max_length=50, unique=False, blank=True, verbose_name='Название во множественном числе')
        ),
        migrations.RunPython(set_name_plural),
        migrations.AlterField(
            model_name='role',
            name='name_plural',
            field=models.CharField(max_length=50, unique=True, blank=False, verbose_name='Название во множественном числе')
        ),
    ]
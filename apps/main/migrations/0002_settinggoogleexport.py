# Generated by Django 3.2.11 on 2022-02-10 16:07

from django.db import migrations

def add_google_settings(apps, schema_editor):

    Setting = apps.get_model("core", "Setting")

    Setting.objects.create(
        field_type="TEXT",
        group="GOOGLE_EXPORT",
        settings_key="SPREADSHEET_ID",
        text="1PB-Rzd46wHpldZptqc7CEn9VNkv3iRJuo9e87Xtpgb4",
        description="id Google таблицы",
    )
    Setting.objects.create(
        field_type="TEXT",
        group="GOOGLE_EXPORT",
        settings_key="SHEET",
        text="Лист1",
        description="Наименование листа Google таблицы",
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_setting_group'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingGoogleExport',
            fields=[
            ],
            options={
                'verbose_name': 'Настройки выгрузки в Google таблицу',
                'verbose_name_plural': 'Настройки выгрузки в Google таблицу',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.setting',),
        ),
        migrations.RunPython(
            add_google_settings,
        )
    ]

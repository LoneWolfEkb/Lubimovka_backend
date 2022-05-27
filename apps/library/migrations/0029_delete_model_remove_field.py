# Generated by Django 3.2.13 on 2022-05-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afisha', '0006_masterclass_performance'),
        ('library', '0028_auto_20220426_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performance',
            name='events',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='persons',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='play',
        ),
        migrations.RemoveField(
            model_name='performance',
            name='project',
        ),
        migrations.RemoveField(
            model_name='performanceimage',
            name='image_ptr',
        ),
        migrations.RemoveField(
            model_name='performanceimage',
            name='performance',
        ),
        migrations.RemoveField(
            model_name='performancemediareview',
            name='performance',
        ),
        migrations.RemoveField(
            model_name='performancereview',
            name='performance',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='events',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='persons',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='play',
        ),
        migrations.RemoveField(
            model_name='reading',
            name='project',
        ),
        migrations.AlterField(
            model_name='teammember',
            name='masterclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='afisha.masterclass', verbose_name='Мастер-класс'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='performance',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='afisha.performance', verbose_name='Спектакль'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='reading',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='afisha.reading', verbose_name='Читка'),
        ),
        migrations.DeleteModel(
            name='MasterClass',
        ),
        migrations.DeleteModel(
            name='Performance',
        ),
        migrations.DeleteModel(
            name='PerformanceImage',
        ),
        migrations.DeleteModel(
            name='PerformanceMediaReview',
        ),
        migrations.DeleteModel(
            name='PerformanceReview',
        ),
        migrations.DeleteModel(
            name='Reading',
        ),
    ]

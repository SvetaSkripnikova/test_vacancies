# Generated by Django 3.2 on 2021-05-09 08:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0035_alter_anketa_result_start'),
    ]

    operations = [
        migrations.AddField(
            model_name='result_osa',
            name='start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result_test',
            name='start',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

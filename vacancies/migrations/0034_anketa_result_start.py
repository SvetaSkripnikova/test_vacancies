# Generated by Django 3.2 on 2021-05-08 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0033_alter_application_osa'),
    ]

    operations = [
        migrations.AddField(
            model_name='anketa_result',
            name='start',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2021-05-08 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0034_anketa_result_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa_result',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

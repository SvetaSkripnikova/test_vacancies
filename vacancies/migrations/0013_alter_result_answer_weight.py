# Generated by Django 3.2 on 2021-05-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0012_alter_anketa_result_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_answer',
            name='weight',
            field=models.FloatField(blank=True, default='0'),
        ),
    ]
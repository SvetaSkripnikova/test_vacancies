# Generated by Django 3.2 on 2021-04-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_anketa_result_status_anketa_type_anketa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.URLField(default='https://place-hold.it/100x60'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.URLField(default='https://place-hold.it/100x60'),
        ),
    ]
# Generated by Django 3.2 on 2021-04-28 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0007_remove_answer_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='time',
        ),
    ]

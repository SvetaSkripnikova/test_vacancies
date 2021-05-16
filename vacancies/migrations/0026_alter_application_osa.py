# Generated by Django 3.2 on 2021-05-07 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0025_alter_application_osa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='osa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='osa_application', to='vacancies.osa'),
        ),
    ]
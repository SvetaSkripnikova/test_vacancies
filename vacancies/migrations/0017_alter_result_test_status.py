# Generated by Django 3.2 on 2021-05-06 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0016_auto_20210506_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result_test',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='status_Result_test', to='vacancies.status_test'),
        ),
    ]
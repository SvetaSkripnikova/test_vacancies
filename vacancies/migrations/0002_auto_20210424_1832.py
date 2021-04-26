# Generated by Django 3.2 on 2021-04-24 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='kandidat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kandidat_application', to='accounts.kandidat'),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_application', to='vacancies.status_application'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_application', to='vacancies.vacancy'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='hr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_vacancy', to='accounts.hr'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_vacancy', to='vacancies.status_vacancy'),
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('deadline', models.IntegerField()),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancy_quiz', to='vacancies.vacancy')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_question', models.CharField(max_length=128)),
                ('type_question', models.CharField(max_length=128)),
                ('is_close', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_question', to='vacancies.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_answer', models.CharField(max_length=128)),
                ('correct', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_answer', to='vacancies.question')),
            ],
        ),
    ]

from django.db import models

# Create your models here.
from accounts.models import Kandidat, Hr


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=3000)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.title


class Status_Vacancy(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    speciality = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="speciality")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")
    status = models.ForeignKey(Status_Vacancy, on_delete=models.CASCADE, related_name="status_vacancy")
    description = models.CharField(max_length=3000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)
    hr = models.ForeignKey(Hr, on_delete=models.CASCADE, related_name="hr_vacancy")

    def __str__(self):
        return self.title


class Status_Application(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Application(models.Model):
    kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE, related_name="kandidat_application")
    status = models.ForeignKey(Status_Application, on_delete=models.CASCADE, related_name="status_application")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_application")


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_quiz")


class Question(models.Model):
    text_question = models.CharField(max_length=128)
    type_question = models.CharField(max_length=128)
    is_close = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_question")


class Answer(models.Model):
    text_answer = models.CharField(max_length=128)
    correct = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_answer")


class Status_Anketa(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Type_Anketa(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Anketa_Result(models.Model):
    type = models.ForeignKey(Type_Anketa, on_delete=models.CASCADE, related_name="type_Anketa_Result")
    status = models.ForeignKey(Status_Anketa, on_delete=models.CASCADE, related_name="status_Anketa_Result")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_Anketa_Result")

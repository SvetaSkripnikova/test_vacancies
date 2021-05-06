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

    def get_quizes(self):
        return self.vacancy_quiz.all()


class Status_Application(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Application(models.Model):
    kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE, related_name="kandidat_application")
    status = models.ForeignKey(Status_Application, on_delete=models.CASCADE, related_name="status_application", default="1")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_application")

    def get_anketa_results(self):
        return self.application_Anketa_Result.all()


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.IntegerField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_quiz")

    def get_questions(self):
        return self.quiz_question.all()


class Question(models.Model):
    num = models.IntegerField()
    text_question = models.CharField(max_length=1000)
    type_question = models.CharField(max_length=128)
    is_close = models.BooleanField(default=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="quiz_question")

    def get_answers(self):
        return self.question_answer.all()


class Answer(models.Model):
    text_answer = models.CharField(max_length=3000)
    correct = models.BooleanField(default=False)
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
    type = models.ForeignKey(Type_Anketa, on_delete=models.CASCADE, related_name="type_Anketa_Result", default="1")
    status = models.ForeignKey(Status_Anketa, on_delete=models.CASCADE, related_name="status_Anketa_Result", default="1")
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_Anketa_Result")

    def get_absolute_url(self):
        fl = self.application.vacancy.get_quizes()
        return "/anketa/%p/questions/%i" % self.id % fl.values_list('id').first()


class Result_answer(models.Model):
    text_result = models.CharField(max_length=3000)
    weight = models.FloatField(blank=True, default="0")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_result_answer")
    anketa_result = models.ForeignKey(Anketa_Result, on_delete=models.CASCADE, related_name="anketa_result_result_answer")

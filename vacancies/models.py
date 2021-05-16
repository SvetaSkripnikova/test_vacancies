from datetime import datetime, timedelta
from itertools import count

from django.db import models

# Create your models here.
from django.utils.timezone import utc

from accounts.models import Kandidat, Hr


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=6000)

    def __str__(self):
        return self.name

    def get_vacancies(self):
        return self.company.all()


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
    description = models.CharField(max_length=6000)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField(auto_now_add=True)
    hr = models.ForeignKey(Hr, on_delete=models.CASCADE, related_name="hr_vacancy")

    def __str__(self):
        return self.title

    def get_quizes(self):
        return self.vacancy_quiz.all()

    def get_tests(self):
        return self.vacancy_test.all()

    def get_applications(self):
        return self.vacancy_application.all()


class Status_Application(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Status_Osa(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Osa(models.Model):
    sait = models.CharField(max_length=128)
    code = models.CharField(max_length=128)
    deadline = models.IntegerField(default=24)
    status = models.ForeignKey(Status_Osa, on_delete=models.CASCADE, related_name="status_osa")

    def get_applications(self):
        return self.osa_application.all()


class Application(models.Model):
    kandidat = models.ForeignKey(Kandidat, on_delete=models.CASCADE, related_name="kandidat_application")
    status = models.ForeignKey(Status_Application, on_delete=models.CASCADE, related_name="status_application", default="1")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_application")
    osa = models.ForeignKey(Osa, on_delete=models.CASCADE, related_name="osa_application", blank=True)

    def get_anketa_results(self):
        return self.application_Anketa_Result.all()

    def get_test_results(self):
        return self.application_Result_test.all()

    def get_osa_results(self):
        return self.application_Result_osa.all()

    @property
    def is_deadline_anketa(self):
        if (self.status.id == 1) & (len(self.application_Anketa_Result.all()) == 1) \
                & (self.application_Anketa_Result.first() != 0):
            finish = self.get_anketa_results().values_list('start')[0][0] + timedelta(
                hours=int(self.vacancy.get_quizes().values_list('deadline')[0][0]))
            if finish <= utc.localize(datetime.now()):
                return True
        else:
            return False

    @property
    def is_deadline_test(self):
        if (self.status.id == 3) & (len(self.application_Result_test.all()) == 1) \
                & (self.application_Result_test.first() != 0):
            finish = self.get_test_results().values_list('start')[0][0] + timedelta(hours=int(self.vacancy.get_tests().values_list('deadline')[0][0]))
            if finish <= utc.localize(datetime.now()):
                return True
        else:
            return False

    @property
    def is_deadline_osa(self):
        if (self.status.id == 5) & (len(self.application_Result_osa.all()) == 1)\
                & (self.application_Result_osa.first() != 0):
            finish = self.get_osa_results().values_list('start')[0][0] + timedelta(hours=self.osa.deadline)
            if finish <= utc.localize(datetime.now()):
                return True
        else:
            return False


class Quiz(models.Model):
    title = models.CharField(max_length=128)
    deadline = models.IntegerField(default=24)
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
    start = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        fl = self.application.vacancy.get_quizes()
        return "/anketa/%p/questions/%i" % self.id % fl.values_list('id').first()


class Result_answer(models.Model):
    text_result = models.CharField(max_length=3000)
    weight = models.FloatField(blank=True, default="0")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="question_result_answer")
    anketa_result = models.ForeignKey(Anketa_Result, on_delete=models.CASCADE, related_name="anketa_result_result_answer")


class Status_Test(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Test(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    deadline = models.IntegerField(default=24)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="vacancy_test")


class Result_test(models.Model):
    text_result = models.CharField(max_length=500)
    status = models.ForeignKey(Status_Test, on_delete=models.CASCADE, related_name="status_Result_test", default=1)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_Result_test")
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="test_result_test")
    start = models.DateTimeField(auto_now_add=True)


class Result_osa(models.Model):
    code = models.CharField(max_length=128)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="application_Result_osa")
    osa = models.ForeignKey(Osa, on_delete=models.CASCADE, related_name="osa_result_osa")
    start = models.DateTimeField(auto_now_add=True)

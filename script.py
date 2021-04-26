from django.core import management
from django.core.serializers import python

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_vacancies.settings")
django.setup()

from vacancies.models import Company, Specialty, Vacancy, Status_Vacancy, \
    Status_Application, Application, Quiz, Question, Answer, Status_Anketa, \
    Type_Anketa, Anketa_Result, Hr, Kandidat
import data as dat

for c in dat.companies:
    Company.objects.create(**c)
for s in dat.specialties:
    Specialty.objects.create(**s)
for s in dat.status_vacancy:
    Status_Vacancy.objects.create(**s)
for j in dat.jobs:
    Vacancy.objects.create(
        title=j["title"],
        description=j["description"],
        published_at=j["published_at"],
        salary_min=j["salary_min"],
        salary_max=j["salary_max"],
        status=Status_Vacancy.objects.filter(id=j["status"]).first(),
        company=Company.objects.filter(id=j["company"]).first(),
        speciality=Specialty.objects.filter(id=j["speciality"]).first(),
        hr=Hr.objects.filter(user_id=j["hr"]).first(),
    )
for s in dat.status_application:
    Status_Application.objects.create(**s)
for a in dat.application:
    Application.objects.create(
        kandidat=Kandidat.objects.filter(user_id=a["kandidat"]).first(),
        status=Status_Application.objects.filter(id=a["status"]).first(),
        vacancy=Vacancy.objects.filter(id=a["vacancy"]).first(),
    )


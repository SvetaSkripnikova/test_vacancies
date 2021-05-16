from django import forms
from django.db import transaction

from vacancies.models import Vacancy, Company


class UpdateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("title", "speciality", "company", "status", "description", "salary_min", "salary_max",)


class CreateVacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("title", "speciality", "company", "status", "description", "salary_min", "salary_max", "hr",)


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name", "location", "logo", "description",)


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ("name", "location", "logo", "description", )



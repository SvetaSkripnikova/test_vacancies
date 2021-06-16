from django import forms

from vacancies.models import Vacancy, Company, Result_answer, Application, Osa, Quiz, Test


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


class UpdateAnswerForm(forms.ModelForm):
    class Meta:
        model = Result_answer
        fields = ("weight",)


class UpdateApplicationAnketaResultForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status",)


class UpdateApplicationTestResultForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status", "osa",)


class UpdateOsaForm(forms.ModelForm):
    class Meta:
        model = Osa
        fields = ("status",)


class CreateOsaForm(forms.ModelForm):
    class Meta:
        model = Osa
        fields = ("sait", "code", "deadline", "status", )


class UpdateApplicationOsaResultForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status", )


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ("title", "deadline", "vacancy", )


class UpdateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ("title", "deadline", "vacancy", )


class CreateTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ("title", "description", "deadline", "vacancy", )


class UpdateTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ("title", "description", "deadline", "vacancy", )


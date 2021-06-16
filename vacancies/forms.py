from django import forms
from django.db import transaction

from vacancies.models import Application, Result_answer, Anketa_Result, Result_test, Result_osa


class ApplyVacancyForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("vacancy", "kandidat", "status", "osa",)

    @transaction.atomic
    def save(self):
        new_apply = super().save()
        new_apply.kandidat = self.cleaned_data["kandidat"]
        new_apply.status = self.cleaned_data["status"]
        new_apply.vacancy = self.cleaned_data["vacancy"]
        new_apply.osa = self.cleaned_data["osa"]
        new_apply.save()
        return new_apply


class StartAnketResultForm(forms.ModelForm):
    class Meta:
        model = Anketa_Result
        fields = ("application",)

    @transaction.atomic
    def save(self):
        new_anketa_result = super().save()
        new_anketa_result.application = self.cleaned_data["application"]
        new_anketa_result.save()
        return new_anketa_result


class UpdateApplicationAnketaForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status",)


class QuestionsForm(forms.ModelForm):
    text_result = forms.CharField(label='text_result')

    class Meta:
        model = Result_answer
        fields = ("text_result", "anketa_result", "question",)

    @transaction.atomic
    def save(self):
        new_result = super().save()
        new_result.text_result = self.cleaned_data["text_result"]
        new_result.question = self.cleaned_data["question"]
        new_result.anketa_result = self.cleaned_data["anketa_result"]
        new_result.save()
        return new_result


class StartTestResultForm(forms.ModelForm):
    class Meta:
        model = Result_test
        fields = ("text_result", "status", "application", "test",)


class UpdateApplicationTestForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status",)


class UpdateTestForm(forms.ModelForm):
    class Meta:
        model = Result_test
        fields = ("text_result", "status",)


class StartOsaResultForm(forms.ModelForm):
    class Meta:
        model = Result_osa
        fields = ("code", "application", "osa",)


class UpdateApplicationOsaForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status",)


class UpdateOsaForm(forms.ModelForm):
    class Meta:
        model = Result_osa
        fields = ("code",)


class UpdateSobesForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status",)

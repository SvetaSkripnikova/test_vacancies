from django import forms
from django.db import transaction

from vacancies.models import Application, Question, Result_answer, Anketa_Result
from accounts.models import User


class ApplyVacancyForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("vacancy", "kandidat", "status")

    @transaction.atomic
    def save(self):
        new_apply = super().save()
        new_apply.kandidat = self.cleaned_data["kandidat"]
        #User.objects.filter(user_id=self.request.user.id)["user_id"]
        new_apply.status = self.cleaned_data["status"]
        new_apply.vacancy = self.cleaned_data["vacancy"]
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


class UpdateAnketResultForm(forms.ModelForm):
    class Meta:
        model = Anketa_Result
        fields = ("status",)

    #@transaction.atomic
    #def save(self):
    #    anketa = super().save()
    #    anketa.status = self.cleaned_data["status"]
    #    anketa.save()
    #    return anketa


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


from django import template

from vacancies.models import Result_answer

register = template.Library()


@register.simple_tag(name="is_already_answered")
def is_already_answered(question, anketa_result):
    answered = Result_answer.objects.filter(question=question, anketa_result=anketa_result)
    if answered:
        return True
    else:
        return False

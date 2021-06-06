from datetime import timedelta, datetime

import pytz
from django import template

from vacancies.models import Anketa_Result, Result_answer

register = template.Library()

utc=pytz.UTC

@register.simple_tag(name="type_result")
def type_result(anketa_result):
    answers = Result_answer.objects.filter(anketa_result__id=anketa_result)
    summ = 0
    for answer in answers:
        summ = summ + answer.weight
    if summ <= 25:
        return True
    else:
        return False

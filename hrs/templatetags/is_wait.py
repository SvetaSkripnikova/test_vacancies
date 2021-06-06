from datetime import timedelta, datetime

import pytz
from django import template

from vacancies.models import Anketa_Result, Result_answer

register = template.Library()

utc=pytz.UTC

@register.simple_tag(name="is_wait")
def is_wait(anketa_result):
    answers = Result_answer.objects.filter(anketa_result__id=anketa_result)
    print(answers)
    fl = True
    for answer in answers.values_list('weight'):
        print(answer)
        if answer == "3":
            return fl
        else:
            fl = False
            return fl

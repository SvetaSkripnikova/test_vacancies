from datetime import timedelta, datetime

import pytz
from django import template

from vacancies.models import Anketa_Result

register = template.Library()

utc=pytz.UTC

@register.simple_tag(name="is_deadline_anketa")
def is_deadline_anketa(application):
    anketa_result = Anketa_Result.objects.filter(application=application).first()
    if anketa_result:
        deadline = anketa_result.application.vacancy.get_quizes().values_list('deadline')[0][0]
        finish = anketa_result.start + timedelta(hours=int(deadline))
        now = utc.localize(datetime.now())
        if (finish <= now) and (anketa_result.application.status.id == 1):
            return True
        else:
            return False
    else:
        return False

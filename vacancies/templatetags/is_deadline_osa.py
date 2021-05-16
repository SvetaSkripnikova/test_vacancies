from datetime import timedelta, datetime

import pytz
from django import template

from vacancies.models import Result_osa

register = template.Library()

utc=pytz.UTC

@register.simple_tag(name="is_deadline_osa")
def is_deadline_osa(application):
    osa_result = Result_osa.objects.filter(application=application).first()
    if osa_result:
        deadline = osa_result.osa.deadline
        finish = osa_result.start + timedelta(hours=int(deadline))
        now = utc.localize(datetime.now())
        if (finish <= now) and (osa_result.application.status.id == 5):
            return True
        else:
            return False
    else:
        return False

from datetime import timedelta, datetime

import pytz
from django import template

from vacancies.models import Result_test

register = template.Library()

utc=pytz.UTC

@register.simple_tag(name="is_deadline_test")
def is_deadline_test(application):
    test_result = Result_test.objects.filter(application=application).first()
    if test_result:
        deadline = test_result.test.deadline
        finish = test_result.start + timedelta(hours=int(deadline))
        now = utc.localize(datetime.now())
        if (finish <= now) and (test_result.application.status.id == 3):
            return True
        else:
            return False
    else:
        return False

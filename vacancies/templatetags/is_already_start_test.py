from django import template

from vacancies.models import Result_test

register = template.Library()


@register.simple_tag(name="is_already_start_test")
def is_already_start_test(application):
    anketa_result = Result_test.objects.filter(application=application)
    if anketa_result:
        return True
    else:
        return False

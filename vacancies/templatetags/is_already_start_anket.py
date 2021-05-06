from django import template

from vacancies.models import Anketa_Result

register = template.Library()


@register.simple_tag(name="is_already_start_anket")
def is_already_start_anket(application):
    anketa_result = Anketa_Result.objects.filter(application=application)
    if anketa_result:
        return True
    else:
        return False

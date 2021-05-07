from django import template

from vacancies.models import Result_osa

register = template.Library()


@register.simple_tag(name="is_already_start_osa")
def is_already_start_osa(application):
    osa_result = Result_osa.objects.filter(application=application)
    if osa_result:
        return True
    else:
        return False

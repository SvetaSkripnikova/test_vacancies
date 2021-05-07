from django import template

from vacancies.models import Result_osa

register = template.Library()


@register.simple_tag(name="is_already_osaed")
def is_already_osaed(application, osa):
    tested = Result_osa.objects.get(application=application, osa=osa)
    if tested.code != "-":
        return True
    else:
        return False

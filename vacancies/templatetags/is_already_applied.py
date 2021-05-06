from django import template

from vacancies.models import Application

register = template.Library()


@register.simple_tag(name="is_already_applied")
def is_already_applied(vacancy, user):
    applied = Application.objects.filter(vacancy=vacancy, kandidat=user)
    if applied:
        return True
    else:
        return False

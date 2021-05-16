from django import template

from vacancies.models import Application

register = template.Library()


@register.simple_tag(name="is_limit_app")
def is_limit_app(kandidat):
    kol_applied = Application.objects.filter(kandidat=kandidat).count()
    print(kol_applied)
    if kol_applied == 3:
        return True
    else:
        return False

from django import template

from vacancies.models import Result_test

register = template.Library()


@register.simple_tag(name="is_already_tested")
def is_already_tested(application, test):
    tested = Result_test.objects.get(application=application, test=test)
    if tested.text_result != "нет ответа":
        return True
    else:
        return False

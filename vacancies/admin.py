from django.contrib import admin

# Register your models here.
from vacancies.models import Anketa_Result, Quiz, Answer, Question

admin.site.register(Anketa_Result)
admin.site.register(Quiz)


class AnswerInLine(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)

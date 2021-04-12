from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
#def home(request):
#    context = {}
#    template = 'index.html'
#    return render(request, template, context)
from django.views import View
from django.views.generic import TemplateView


class MainView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        #context["specialities"] = Specialty.objects.annotate(vacancies_Count=Count('vacancies'))
        #context["companies"] = Company.objects.annotate(vacancies_Count=Count('vacancies'))
        return context






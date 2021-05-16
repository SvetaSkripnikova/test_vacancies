from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect, request
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
#def home(request):
#    context = {}
#    template = 'index.html'
#    return render(request, template, context)
from django.urls import reverse_lazy, resolve
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

from accounts.models import Kandidat
from vacancies.forms import ApplyVacancyForm, StartAnketResultForm, QuestionsForm, \
    UpdateApplicationAnketaForm, StartTestResultForm, UpdateApplicationTestForm, UpdateTestForm, StartOsaResultForm, \
    UpdateOsaForm, UpdateApplicationOsaForm
from vacancies.models import Specialty, Company, Vacancy, Application, Status_Application, Question, Quiz, \
    Anketa_Result, Result_answer, Status_Anketa, Result_test, Test, Osa, Result_osa


class MainView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["specialities"] = Specialty.objects.annotate(vacancies_Count=Count('speciality'))
        context["companies"] = Company.objects.annotate(vacancies_Count=Count('company'))
        return context


class DetailCompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(DetailCompanyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["vacancies"] = Vacancy.objects.filter(company__id=self.kwargs["pk"])
        context["speciality_list"] = Specialty.objects.all()
        return context


class DetailVacancyView(DetailView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(DetailVacancyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ApplyVacancyView(CreateView):
    model = Application
    form_class = ApplyVacancyForm
    slug_field = "vacancy_id"
    slug_url_kwarg = "vacancy_id"

    #@method_decorator(login_required(login_url=reverse_lazy("login")))
    #def dispatch(self, request, *args, **kwargs):
    #    return super().dispatch(self.request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy("home"))

    def get_success_url(self):
        return reverse_lazy("vacancy_detail", kwargs={"pk": self.kwargs["vacancy_id"]})

    def form_valid(self, form):
        # check if user already applied
        applicant = Application.objects.filter(kandidat=self.request.user.id, vacancy=self.kwargs["vacancy_id"])
        if applicant:
            return HttpResponseRedirect(self.get_success_url())
        # save applicant
        form.instance.kandidat = Kandidat.objects.get(user=self.request.user.id)
        form.instance.status = Status_Application.objects.get(code="wait1")
        form.save()
        return super().form_valid(form)


class ListVacanciesView(ListView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(ListVacanciesView, self).get_context_data(**kwargs)
        context["title"] = "Все вакансии"
        context["object_list"] = Vacancy.objects.all()
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ListCategoriesView(ListView):
    model = Vacancy
    context_object_name = "vacancy_list"

    def get_context_data(self, **kwargs):
        context = super(ListCategoriesView, self).get_context_data(**kwargs)
        context["title"] = get_object_or_404(Specialty, code=self.kwargs["code"]).title
        context["object_list"] = Vacancy.objects.filter(speciality__title=context["title"])
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ApplicationsListView(ListView):
    model = Application
    template_name = "vacancies/applications_list.html"
    context_object_name = "applications"
    paginate_by = 6

    def get_success_url(self):
        return reverse_lazy('questions', kwargs={'id': self.request.get_anketa_results.first.pk, 'pk': self.vacancy.get_quizes().values_list('id').first()}, params={'page':'1'})

    def get_queryset(self):
        self.queryset = (
            self.model.objects.select_related("vacancy").filter(kandidat=self.request.user.id)
        )
        if (
            "status" in self.request.GET
            and len(self.request.GET.get("status")) > 0
            and int(self.request.GET.get("status")) > 0
        ):
            self.queryset = self.queryset.filter(status=int(self.request.GET.get("status")))
        return self.queryset


class StartAnketaResultView(CreateView):
    model = Anketa_Result
    template_name = "vacancies/questions_list.html"
    form_class = StartAnketResultForm

    def get_success_url(self):
        return reverse_lazy('questions', kwargs={'id': self.object.pk, 'pk': int(self.object.application.vacancy.get_quizes().values_list('id')[0][0])}) + '?page='+str(1)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy("home"))

    def form_valid(self, form):
        # save start anketa_result
        form.save()
        return super().form_valid(form)


class UpdateApplicationAnketaView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "vacancies/questions_list.html"
    form_class = UpdateApplicationAnketaForm

    def get_success_url(self):
        return reverse_lazy('applications')


class QuestionsListView(ListView):
    model = Question
    template_name = "vacancies/questions_list.html"
    context_object_name = "questions"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(QuestionsListView, self).get_context_data(**kwargs)
        context["questions_list"] = Question.objects.filter(quiz__pk=self.kwargs["pk"])
        context["qw_kol"] = Question.objects.filter(quiz__pk=self.kwargs["pk"]).count
        context["title"] = get_object_or_404(Quiz, pk=self.kwargs["pk"]).title
        context["deadline"] = get_object_or_404(Quiz, pk=self.kwargs["pk"]).deadline
        context["id"] = get_object_or_404(Anketa_Result, id=self.kwargs["id"]).pk
        context["start"] = get_object_or_404(Anketa_Result, id=self.kwargs["id"]).start
        context["id_app"] = get_object_or_404(Anketa_Result, id=self.kwargs["id"]).application.pk
        return context

    def get_queryset(self):
        questions = Question.objects.filter(quiz__pk=self.kwargs["pk"])
        return questions


class CreateAnswer(CreateView):
    model = Result_answer
    template_name = "vacancies/questions_list.html"
    form_class = QuestionsForm

    def get_success_url(self):
        next_url=self.object.question.num
        return reverse_lazy('questions', kwargs={'id': self.object.anketa_result.pk, 'pk': int(self.object.anketa_result.application.vacancy.get_quizes().values_list('id')[0][0])}) + '?page='+str(next_url)

    def get(self, request, *args, **kwargs):
        next_url=self.object.question.num
        return reverse_lazy('questions', kwargs={'id': self.object.anketa_result.pk, 'pk': int(self.object.anketa_result.application.vacancy.get_quizes().values_list('id')[0][0])}) + '?page='+str(next_url)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return HttpResponseRedirect(reverse_lazy('questions', kwargs={'id': self.request.id, 'pk': self.request.pk}))


class DetailTestView(DetailView):
    model = Test
    template_name = "vacancies/test_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailTestView, self).get_context_data(**kwargs)
        context["app"] = Application.objects.get(id=self.kwargs["id"])
        #context["id"] = get_object_or_404(Application, id=self.kwargs["id"]).pk
        return context


class StartTestResultView(CreateView):
    model = Result_test
    template_name = "vacancies/test_detail.html"
    form_class = StartTestResultForm

    def get_success_url(self):
        return reverse_lazy('test_detail', kwargs={'id': self.object.application.pk, 'pk': self.object.test.pk})


class UpdateTestView(UpdateView):
    model = Result_test
    pk_url_kwarg = 'pk'
    template_name = "vacancies/test_detail.html"
    form_class = UpdateTestForm

    def get_success_url(self):
        return reverse_lazy('test_detail', kwargs={'id': self.object.application.pk, 'pk': self.object.test.pk})


class UpdateApplicationTestView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "vacancies/test_detail.html"
    form_class = UpdateApplicationTestForm

    def get_success_url(self):
        return reverse_lazy('applications')


class DetailOsaView(DetailView):
    model = Osa
    template_name = "vacancies/osa_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailOsaView, self).get_context_data(**kwargs)
        context["app"] = Application.objects.get(id=self.kwargs["id"])
        return context


class StartOsaResultView(CreateView):
    model = Result_osa
    template_name = "vacancies/osa_detail.html"
    form_class = StartOsaResultForm

    def get_success_url(self):
        return reverse_lazy('osa_detail', kwargs={'id': self.object.application.pk, 'pk': self.object.osa.pk})


class UpdateOsaView(UpdateView):
    model = Result_osa
    pk_url_kwarg = 'pk'
    template_name = "vacancies/osa_detail.html"
    form_class = UpdateOsaForm

    def get_success_url(self):
        return reverse_lazy('osa_detail', kwargs={'id': self.object.application.pk, 'pk': self.object.osa.pk})


class UpdateApplicationOsaView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "vacancies/osa_detail.html"
    form_class = UpdateApplicationOsaForm

    def get_success_url(self):
        return reverse_lazy('applications')

from django.db.models import Count
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from hrs.forms import UpdateVacancyForm, CreateVacancyForm, UpdateCompanyForm, CreateCompanyForm, UpdateAnswerForm, \
    UpdateApplicationAnketaResultForm, UpdateApplicationTestResultForm, CreateOsaForm, UpdateOsaForm, \
    UpdateApplicationOsaResultForm, CreateQuizForm, UpdateQuizForm, UpdateTestForm, CreateTestForm
from vacancies.forms import UpdateSobesForm
from vacancies.models import Vacancy, Company, Specialty, Status_Vacancy, Application, Result_answer, Anketa_Result, \
    Result_test, Osa, Result_osa, Quiz, Test


class ListVacanciesHRView(ListView):
    model = Vacancy
    template_name = "hrs/vacancies_hr_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListVacanciesHRView, self).get_context_data(**kwargs)
        context["title"] = "Все вакансии"
        context["object_list"] = Vacancy.objects.all()
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ListCompaniesHRView(ListView):
    model = Company
    template_name = "hrs/companies_hr_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListCompaniesHRView, self).get_context_data(**kwargs)
        context["object_list"] = Company.objects.all()
        return context


class DetailVacanciesCompanyView(DetailView):
    model = Company
    template_name = "hrs/vacancies_company_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailVacanciesCompanyView, self).get_context_data(**kwargs)
        context["vacancies"] = Vacancy.objects.filter(company__id=self.kwargs["pk"])
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ListApplicationsAnketaView(ListView):
    model = Anketa_Result
    template_name = "hrs/applications_anketa_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListApplicationsAnketaView, self).get_context_data(**kwargs)
        context["anketa_results"] = Anketa_Result.objects.filter(application__vacancy__id=self.kwargs["pk"], application__status__id="2")
        context["vacancy"] = get_object_or_404(Vacancy, pk=self.kwargs["pk"])
        return context


class DetailApplicationsVacancyView(DetailView):
    model = Vacancy
    template_name = "hrs/applications_vacancy_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailApplicationsVacancyView, self).get_context_data(**kwargs)
        context["apps_all"] = Application.objects.filter(vacancy__id=self.kwargs["pk"])
        context["apps_go_anket"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="1")
        context["apps_go_test"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="3")
        context["apps_go_osa"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="5")
        context["apps_anket"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="2")
        context["apps_test"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="4")
        context["apps_osa"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="6")
        context["apps_check_sobes"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="7")
        context["apps_go_sobes"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="8")
        context["apps_win"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="9")
        context["apps_fail"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="10")

        context["fail_anket"] = len([x.id for x in Application.objects.all() if x.is_deadline_anketa == True and x.vacancy.id == self.kwargs["pk"]])
        context["fail_test"] = len([x.id for x in Application.objects.all() if x.is_deadline_test == True and x.vacancy.id == self.kwargs["pk"]])
        context["fail_osa"] = len([x.id for x in Application.objects.all() if x.is_deadline_osa == True and x.vacancy.id == self.kwargs["pk"]])

        context["check_anket"] = len(context["apps_go_anket"]) - context["fail_anket"]
        context["check_test"] = len(context["apps_go_test"]) - context["fail_test"]
        context["check_osa"] = len(context["apps_go_osa"]) - context["fail_osa"]

        context["count_go_anket"] = int((context["check_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_anket"] = int(
            int((context["check_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_test"] = int((context["check_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_test"] = int(int((context["check_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_osa"] = int((context["check_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_osa"] = int(int((context["check_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_anket"] = int(len(context["apps_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_anket"] = int(
            int(len(context["apps_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_test"] = int(len(context["apps_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_test"] = int(
            int(len(context["apps_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_osa"] = int(len(context["apps_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_osa"] = int(
            int(len(context["apps_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_anket"] = int((context["fail_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_anket"] = int(
            int((context["fail_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_test"] = int((context["fail_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_test"] = int(
            int((context["fail_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_osa"] = int((context["fail_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_osa"] = int(int((context["fail_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_check_sobes"] = int(len(context["apps_check_sobes"]) / len(context["apps_all"]) * 100)
        context["progress_count_check_sobes"] = int(
            int(len(context["apps_check_sobes"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_sobes"] = int(len(context["apps_go_sobes"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_sobes"] = int(
            int(len(context["apps_go_sobes"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_win"] = int(len(context["apps_win"]) / len(context["apps_all"]) * 100)
        context["progress_count_win"] = int(int(len(context["apps_win"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail"] = int(len(context["apps_fail"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail"] = int(int(len(context["apps_fail"]) / len(context["apps_all"]) * 100) / 25) * 25
        return context


class UpdateVacancyView(UpdateView):
    model = Vacancy
    pk_url_kwarg = 'pk'
    template_name = "update_vacancy.html"
    form_class = UpdateVacancyForm

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')

    def get_context_data(self, **kwargs):
        context = super(UpdateVacancyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        context["status_list"] = Status_Vacancy.objects.all()
        return context


class CreateVacancyView(CreateView):
    model = Vacancy
    form_class = CreateVacancyForm
    template_name = "create_vacancy.html"

    def get_context_data(self, **kwargs):
        context = super(CreateVacancyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        context["status_list"] = Status_Vacancy.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')


class DeleteVacancyView(DeleteView):
    model = Vacancy
    pk_url_kwarg = 'pk'
    template_name = "update_vacancy.html"

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')


class CreateCompanyView(CreateView):
    model = Company
    template_name = "create_company.html"
    form_class = CreateCompanyForm

    def get_success_url(self):
        return reverse_lazy('companies-hr')


class UpdateCompanyView(UpdateView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = "update_company.html"
    form_class = UpdateCompanyForm

    def get_success_url(self):
        return reverse_lazy('companies-hr')


class DeleteCompanyView(DeleteView):
    model = Company
    pk_url_kwarg = 'pk'
    template_name = "update_company.html"

    def get_success_url(self):
        return reverse_lazy('companies-hr')


class ResultAnswersListView(ListView):
    model = Result_answer
    template_name = "hrs/result_answers_list.html"
    context_object_name = "answers"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(ResultAnswersListView, self).get_context_data(**kwargs)
        context["answers_list"] = Result_answer.objects.filter(anketa_result__pk=self.kwargs["pk"])
        context["answ_kol"] = Result_answer.objects.filter(anketa_result__pk=self.kwargs["pk"]).count
        context["title"] = get_object_or_404(Anketa_Result, pk=self.kwargs["pk"]).application.vacancy.title
        return context

    def get_queryset(self):
        answers = Result_answer.objects.filter(anketa_result__pk=self.kwargs["pk"])
        return answers


class UpdateAnswerView(UpdateView):
    model = Result_answer
    template_name = "hrs/result_answers_list.html"
    slug_url_kwarg = 'id'
    form_class = UpdateAnswerForm

    def get_success_url(self):
        next_url = self.object.question.num
        return reverse_lazy('marks', kwargs={'pk': self.object.anketa_result.pk, 'id': self.object.pk})+ '?page='+str(next_url)


class UpdateApplicationAnketaResultView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "type_result.html"
    form_class = UpdateApplicationAnketaResultForm

    def get_success_url(self):
        return reverse_lazy('applications-vacancy', kwargs={'pk': self.object.vacancy.pk})


class UpdateApplicationTestResultView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "test_result.html"
    form_class = UpdateApplicationTestResultForm

    def get_success_url(self):
        return reverse_lazy('test-result', kwargs={'pk': str(self.object.get_test_results().values_list('id').first()[0]), 'id': self.object.pk})


class TypeResultView(DetailView):
    model = Anketa_Result
    template_name = "type_result.html"

    def get_context_data(self, **kwargs):
        context = super(TypeResultView, self).get_context_data(**kwargs)
        context["title"] = get_object_or_404(Anketa_Result, pk=self.kwargs["pk"]).application.vacancy.title
        context["answers"] = Result_answer.objects.filter(anketa_result__id=self.kwargs["pk"])
        context["an"] = 0
        context["fl"] = 0
        return context


class DetailTestResultView(DetailView):
    model = Result_test
    template_name = "hrs/test_result_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailTestResultView, self).get_context_data(**kwargs)
        context["result_test"] = get_object_or_404(Result_test, pk=self.kwargs["pk"])
        context["title"] = get_object_or_404(Result_test, pk=self.kwargs["pk"]).application.vacancy.title
        context["osa"] = Osa.objects.filter(status__id="1")
        return context


class ListApplicationsTestView(ListView):
    model = Result_test
    template_name = "hrs/applications_test_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListApplicationsTestView, self).get_context_data(**kwargs)
        context["test_results"] = Result_test.objects.filter(application__vacancy__id=self.kwargs["pk"], application__status__id="4")
        context["vacancy"] = get_object_or_404(Vacancy, pk=self.kwargs["pk"])
        return context


class ListOsaView(ListView):
    model = Osa
    template_name = "hrs/osa_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListOsaView, self).get_context_data(**kwargs)
        context["free"] = len(Osa.objects.filter(status__id="1"))
        context["object_list"] = Osa.objects.all()
        context["kol"] = len(Osa.objects.all())-1
        return context


class CreateOsaView(CreateView):
    model = Osa
    template_name = "hrs/osa_list.html"
    form_class = CreateOsaForm

    def get_success_url(self):
        return reverse_lazy('OSA-hr')


class UpdateOsaView(UpdateView):
    model = Osa
    pk_url_kwarg = 'pk'
    template_name = "hrs/applications_test_list.html"
    form_class = UpdateOsaForm

    def get_success_url(self):
        return reverse_lazy('home')


class ListApplicationsOsaView(ListView):
    model = Result_osa
    template_name = "hrs/applications_osa_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListApplicationsOsaView, self).get_context_data(**kwargs)
        context["osa_results"] = Result_osa.objects.filter(application__vacancy__id=self.kwargs["pk"], application__status__id="6")
        context["vacancy"] = get_object_or_404(Vacancy, pk=self.kwargs["pk"])
        return context


class DetailOsaResultView(DetailView):
    model = Result_osa
    template_name = "hrs/osa_result_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailOsaResultView, self).get_context_data(**kwargs)
        context["result_osa"] = get_object_or_404(Result_osa, pk=self.kwargs["pk"])
        context["title"] = get_object_or_404(Result_osa, pk=self.kwargs["pk"]).application.vacancy.title
        return context


class UpdateApplicationOsaResultView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "osa_result.html"
    form_class = UpdateApplicationOsaResultForm

    def get_success_url(self):
        return reverse_lazy('osa-result', kwargs={'pk': str(self.object.get_osa_results().values_list('id').first()[0]), 'id': self.object.pk})


class ListApplicationsSobesView(ListView):
    model = Application
    template_name = "hrs/applications_sobes_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListApplicationsSobesView, self).get_context_data(**kwargs)
        context["sobes"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="7")
        context["vacancy"] = get_object_or_404(Vacancy, pk=self.kwargs["pk"])
        return context


class DetailSobesView(DetailView):
    model = Application
    template_name = "hrs/sobes_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailSobesView, self).get_context_data(**kwargs)
        context["sobes"] = get_object_or_404(Application, pk=self.kwargs["pk"])
        context["title"] = get_object_or_404(Application, pk=self.kwargs["pk"]).vacancy.title
        return context


class UpdateApplicationSobesView(UpdateView):
    model = Application
    pk_url_kwarg = 'pk'
    template_name = "hrs/sobes_detail.html"
    form_class = UpdateSobesForm

    def get_success_url(self):
        return reverse_lazy('applications-vacancy', kwargs={'pk': self.object.vacancy.pk})


class ListApplicationsResultSobesView(ListView):
    model = Application
    template_name = "hrs/applications_result_sobes_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListApplicationsResultSobesView, self).get_context_data(**kwargs)
        context["sobes"] = Application.objects.filter(vacancy__id=self.kwargs["pk"], status__id="8")
        context["vacancy"] = get_object_or_404(Vacancy, pk=self.kwargs["pk"])
        return context


class DetailSobesResultView(DetailView):
    model = Application
    template_name = "hrs/sobes_result_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailSobesResultView, self).get_context_data(**kwargs)
        context["sobes"] = get_object_or_404(Application, pk=self.kwargs["pk"])
        context["title"] = get_object_or_404(Application, pk=self.kwargs["pk"]).vacancy.title
        return context


class ListAllApplicationsHRView(ListView):
    model = Application
    template_name = "hrs/applications_hr_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListAllApplicationsHRView, self).get_context_data(**kwargs)
        context["apps_all"] = Application.objects.all()
        context["vacancies"] = Vacancy.objects.all()

        context["al_anket"] = Vacancy.objects.annotate(
            applications_Count=Count('vacancy_application')).order_by('-applications_Count')

        context["apps_go_anket"] = Application.objects.filter(status__id="1")
        context["apps_go_test"] = Application.objects.filter(status__id="3")
        context["apps_go_osa"] = Application.objects.filter(status__id="5")
        context["apps_anket"] = Application.objects.filter(status__id="2")
        context["apps_test"] = Application.objects.filter(status__id="4")
        context["apps_osa"] = Application.objects.filter(status__id="6")
        context["apps_check_sobes"] = Application.objects.filter(status__id="7")
        context["apps_go_sobes"] = Application.objects.filter(status__id="8")
        context["apps_win"] = Application.objects.filter(status__id="9")
        context["apps_fail"] = Application.objects.filter(status__id="10")

        context["fail_anket"] = len([x.id for x in Application.objects.all() if x.is_deadline_anketa == True])
        context["fail_test"] = len([x.id for x in Application.objects.all() if x.is_deadline_test == True])
        context["fail_osa"] = len([x.id for x in Application.objects.all() if x.is_deadline_osa == True])

        context["check_anket"] = len(context["apps_go_anket"]) - context["fail_anket"]
        context["check_test"] = len(context["apps_go_test"]) - context["fail_test"]
        context["check_osa"] = len(context["apps_go_osa"]) - context["fail_osa"]

        context["count_go_anket"] = int((context["check_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_anket"] = int(int((context["check_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_test"] = int((context["check_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_test"] = int(int((context["check_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_osa"] = int((context["check_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_osa"] = int(int((context["check_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_anket"] = int(len(context["apps_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_anket"] = int(int(len(context["apps_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_test"] = int(len(context["apps_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_test"] = int(int(len(context["apps_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_wait_osa"] = int(len(context["apps_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_wait_osa"] = int(int(len(context["apps_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_anket"] = int((context["fail_anket"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_anket"] = int(int((context["fail_anket"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_test"] = int((context["fail_test"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_test"] = int(int((context["fail_test"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail_osa"] = int((context["fail_osa"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail_osa"] = int(int((context["fail_osa"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_check_sobes"] = int(len(context["apps_check_sobes"]) / len(context["apps_all"]) * 100)
        context["progress_count_check_sobes"] = int(int(len(context["apps_check_sobes"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_go_sobes"] = int(len(context["apps_go_sobes"]) / len(context["apps_all"]) * 100)
        context["progress_count_go_sobes"] = int(int(len(context["apps_go_sobes"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_win"] = int(len(context["apps_win"]) / len(context["apps_all"]) * 100)
        context["progress_count_win"] = int(int(len(context["apps_win"]) / len(context["apps_all"]) * 100) / 25) * 25
        context["count_fail"] = int(len(context["apps_fail"]) / len(context["apps_all"]) * 100)
        context["progress_count_fail"] = int(int(len(context["apps_fail"]) / len(context["apps_all"]) * 100) / 25) * 25
        return context


class CreateQuizView(CreateView):
    model = Quiz
    form_class = CreateQuizForm
    template_name = "create_quiz.html"

    def get_context_data(self, **kwargs):
        context = super(CreateQuizView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')


class UpdateQuizView(UpdateView):
    model = Quiz
    pk_url_kwarg = 'pk'
    template_name = "update_quiz.html"
    form_class = UpdateQuizForm

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')

    def get_context_data(self, **kwargs):
        context = super(UpdateQuizView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.all()
        return context


class DeleteQuizView(DeleteView):
    model = Quiz
    pk_url_kwarg = 'pk'
    template_name = "update_quiz.html"

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')


class CreateTestView(CreateView):
    model = Test
    form_class = CreateTestForm
    template_name = "create_test.html"

    def get_context_data(self, **kwargs):
        context = super(CreateTestView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')


class UpdateTestView(UpdateView):
    model = Test
    pk_url_kwarg = 'pk'
    template_name = "update_test.html"
    form_class = UpdateTestForm

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')

    def get_context_data(self, **kwargs):
        context = super(UpdateTestView, self).get_context_data(**kwargs)
        context["vacancy_list"] = Vacancy.objects.all()
        return context


class DeleteTestView(DeleteView):
    model = Test
    pk_url_kwarg = 'pk'
    template_name = "update_test.html"

    def get_success_url(self):
        return reverse_lazy('vacancies-hr')

from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from hrs.forms import UpdateVacancyForm, CreateVacancyForm, UpdateCompanyForm, CreateCompanyForm
from vacancies.models import Vacancy, Company, Specialty, Status_Vacancy, Application


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
        context["fail_anket"] = len([x.id for x in Application.objects.all() if x.is_deadline_anketa == True and x.vacancy.id == self.kwargs["pk"]])
        context["fail_test"] = len([x.id for x in Application.objects.all() if x.is_deadline_test == True and x.vacancy.id == self.kwargs["pk"]])
        context["fail_osa"] = len([x.id for x in Application.objects.all() if x.is_deadline_osa == True and x.vacancy.id == self.kwargs["pk"]])

        context["count_go_anket"] = len(context["apps_go_anket"]) / len(context["apps_all"]) * 100
        context["count_fail_osa"] = (context["fail_osa"]) / len(context["apps_all"]) * 100
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

from django.urls import path

from accounts import views
from hrs.views import ListVacanciesHRView, UpdateVacancyView, CreateVacancyView, DeleteVacancyView, UpdateCompanyView, \
    DeleteCompanyView, CreateCompanyView, ListCompaniesHRView, DetailVacanciesCompanyView, DetailApplicationsVacancyView

urlpatterns = [
    path('vacancies_hr/', ListVacanciesHRView.as_view(), name="vacancies-hr"),
    path('update_vacancy/<int:pk>', UpdateVacancyView.as_view(), name="update-vacancy"),
    path('create_vacancy/', CreateVacancyView.as_view(), name="create-vacancy"),
    path('delete_vacancy/<int:pk>', DeleteVacancyView.as_view(), name="delete-vacancy"),

    path('companies_hr/', ListCompaniesHRView.as_view(), name="companies-hr"),
    path('update_company/<int:pk>', UpdateCompanyView.as_view(), name="update-company"),
    path('delete_company/<int:pk>', DeleteCompanyView.as_view(), name="delete-company"),
    path('create_company/', CreateCompanyView.as_view(), name="create-company"),
    path('vacancies_hr/company/<int:pk>', DetailVacanciesCompanyView.as_view(), name="vacancies-company"),
    path('applications_hr/vacancy/<int:pk>', DetailApplicationsVacancyView.as_view(), name="applications-vacancy"),
]

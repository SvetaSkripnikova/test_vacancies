"""test_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from test_vacancies import settings
from vacancies import views
from vacancies.forms import StartTestResultForm
from vacancies.views import DetailCompanyView, DetailVacancyView, ListVacanciesView, ListCategoriesView, \
    ApplyVacancyView, ApplicationsListView, QuestionsListView, StartAnketaResultView, CreateAnswer, \
    UpdateApplicationAnketaView, DetailTestView, StartTestResultView, UpdateApplicationTestView, UpdateTestView, \
    StartOsaResultView, DetailOsaView, UpdateApplicationOsaView, UpdateOsaView

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('companies/<int:pk>', DetailCompanyView.as_view(), name="company_detail"),
    path('vacancies/<int:pk>', DetailVacancyView.as_view(), name="vacancy_detail"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/cat/<str:code>', ListCategoriesView.as_view(), name="categories"),

    path("apply_vacancy/<int:vacancy_id>/", ApplyVacancyView.as_view(), name="apply-vacancy"),
    path("anketa_result/<int:application_id>/", StartAnketaResultView.as_view(), name="start-anketa_result"),
    path("application_anketa_update/<int:pk>/", UpdateApplicationAnketaView.as_view(), name="application_anketa_update"),
    path("applications/", ApplicationsListView.as_view(), name="applications"),
    path('anketa/<int:id>/questions/<int:pk>/', QuestionsListView.as_view(), name="questions"),
    path("answer/<int:id>/", CreateAnswer.as_view(), name="answer"),

    path("test_result/<int:application_id>/", StartTestResultView.as_view(), name="start_test_result"),
    path('application/<int:id>/test/<int:pk>', DetailTestView.as_view(), name="test_detail"),
    path("application_test_update/<int:pk>/", UpdateApplicationTestView.as_view(), name="application_test_update"),
    path("test_result_update/<int:pk>/", UpdateTestView.as_view(), name="test_result_update"),

    path("osa_result/<int:application_id>/", StartOsaResultView.as_view(), name="start_osa_result"),
    path('application/<int:id>/osa/<int:pk>', DetailOsaView.as_view(), name="osa_detail"),
    path("application_osa_update/<int:pk>/", UpdateApplicationOsaView.as_view(), name="application_osa_update"),
    path("osa_result_update/<int:pk>/", UpdateOsaView.as_view(), name="osa_result_update"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

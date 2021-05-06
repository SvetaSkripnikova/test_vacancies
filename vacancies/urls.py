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
from django.contrib import admin
from django.urls import path, re_path
from vacancies import views
from vacancies.views import DetailCompanyView, DetailVacancyView, ListVacanciesView, ListCategoriesView, \
    ApplyVacancyView, ApplicationsListView, QuestionsListView, StartAnketaResultView, CreateAnswer, \
    UpdateAnketaResultView

urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('companies/<int:pk>', DetailCompanyView.as_view(), name="company_detail"),
    path('vacancies/<int:pk>', DetailVacancyView.as_view(), name="vacancy_detail"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/cat/<str:code>', ListCategoriesView.as_view(), name="categories"),

    path("apply_vacancy/<int:vacancy_id>/", ApplyVacancyView.as_view(), name="apply-vacancy"),
    path("anketa_result/<int:application_id>/", StartAnketaResultView.as_view(), name="start-anketa_result"),
    path("anketa_update_result/<int:pk>/", UpdateAnketaResultView.as_view(), name="update_anketa_res"),
    path("applications/", ApplicationsListView.as_view(), name="applications"),
    #re_path(r'^anketa/(?P<id>\d+)/questions/(?P<pk>\d+)/(?:/(?P<page>\d+|))/$', QuestionsListView.as_view(), name="questions"),
    #re_path(r'^anketa/<id>/questions/<pk>/?<page>/)', QuestionsListView.as_view(), name="questions"),
    #url(r'^anketa/(?P<id>\d+)/questions/(?P<pk>\d+)(?:/(?P<page>\d+))?/$', CreateAnswer.as_view(), name="answer"),
    path('anketa/<int:id>/questions/<int:pk>/', QuestionsListView.as_view(), name="questions"),
    path("answer/<int:id>/", CreateAnswer.as_view(), name="answer"),
]

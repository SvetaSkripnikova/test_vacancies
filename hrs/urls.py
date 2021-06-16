from django.urls import path

from hrs.views import ListVacanciesHRView, UpdateVacancyView, CreateVacancyView, DeleteVacancyView, UpdateCompanyView, \
    DeleteCompanyView, CreateCompanyView, ListCompaniesHRView, DetailVacanciesCompanyView, \
    DetailApplicationsVacancyView, ResultAnswersListView, ListApplicationsAnketaView, UpdateAnswerView, TypeResultView, \
    UpdateApplicationAnketaResultView, UpdateApplicationTestResultView, DetailTestResultView, ListApplicationsTestView, \
    ListOsaView, CreateOsaView, UpdateOsaView, ListApplicationsOsaView, DetailOsaResultView, \
    UpdateApplicationOsaResultView, ListApplicationsSobesView, DetailSobesView, UpdateApplicationSobesView, \
    ListApplicationsResultSobesView, DetailSobesResultView, ListAllApplicationsHRView, CreateQuizView, UpdateQuizView, \
    DeleteQuizView, CreateTestView, UpdateTestView, DeleteTestView

urlpatterns = [
    path('vacancies_hr/', ListVacanciesHRView.as_view(), name="vacancies-hr"),
    path('update_vacancy/<int:pk>', UpdateVacancyView.as_view(), name="update-vacancy"),
    path('create_vacancy/', CreateVacancyView.as_view(), name="create-vacancy"),
    path('delete_vacancy/<int:pk>', DeleteVacancyView.as_view(), name="delete-vacancy"),

    path('create_quiz/', CreateQuizView.as_view(), name="create-quiz"),
    path('update_quiz/<int:pk>', UpdateQuizView.as_view(), name="update-quiz"),
    path('delete_quiz/<int:pk>', DeleteQuizView.as_view(), name="delete-quiz"),

    path('create_test/', CreateTestView.as_view(), name="create-test"),
    path('update_test/<int:pk>', UpdateTestView.as_view(), name="update-test"),
    path('delete_test/<int:pk>', DeleteTestView.as_view(), name="delete-test"),

    path('applications_hr_all/', ListAllApplicationsHRView.as_view(), name="applications-hr-all"),

    path('companies_hr/', ListCompaniesHRView.as_view(), name="companies-hr"),
    path('update_company/<int:pk>', UpdateCompanyView.as_view(), name="update-company"),
    path('delete_company/<int:pk>', DeleteCompanyView.as_view(), name="delete-company"),
    path('create_company/', CreateCompanyView.as_view(), name="create-company"),
    path('vacancies_hr/company/<int:pk>', DetailVacanciesCompanyView.as_view(), name="vacancies-company"),
    path('applications_hr/vacancy/<int:pk>', DetailApplicationsVacancyView.as_view(), name="applications-vacancy"),

    path('OSA_hr/', ListOsaView.as_view(), name="OSA-hr"),
    path('create_osa/', CreateOsaView.as_view(), name="create-osa"),
    path('update_osa/<int:pk>', UpdateOsaView.as_view(), name="update-osa-hr"),

    path('answers/result_anketa/<int:pk>/result_answer/<int:id>', ResultAnswersListView.as_view(), name="marks"),
    path('applications_anketa/vacancy/<int:pk>', ListApplicationsAnketaView.as_view(), name="applications-anketa"),

    path('result_anketa/<int:pk>/application/<int:id>', TypeResultView.as_view(), name="type-result"),
    path('update_answer/<int:pk>', UpdateAnswerView.as_view(), name="update-answer"),
    path('update_anketa_result_application/<int:pk>', UpdateApplicationAnketaResultView.as_view(), name="update-anketa-result-application"),

    path('applications_test/vacancy/<int:pk>', ListApplicationsTestView.as_view(), name="applications-test"),
    path('result_test/<int:pk>/application/<int:id>', DetailTestResultView.as_view(), name="test-result"),
    path('update_test_result_application/<int:pk>', UpdateApplicationTestResultView.as_view(), name="update-test-result-application"),

    path('applications_osa/vacancy/<int:pk>', ListApplicationsOsaView.as_view(), name="applications-osa"),
    path('result_osa/<int:pk>/application/<int:id>', DetailOsaResultView.as_view(), name="osa-result"),
    path('update_osa_result_application/<int:pk>', UpdateApplicationOsaResultView.as_view(), name="update-osa-result-application"),

    path('applications_sobes/vacancy/<int:pk>', ListApplicationsSobesView.as_view(), name="applications-sobes"),
    path('sobes/application/<int:pk>', DetailSobesView.as_view(), name="sobes-result"),
    path('update_sobes_application/<int:pk>', UpdateApplicationSobesView.as_view(),
         name="update-sobes-application"),

    path('applications_result_sobes/vacancy/<int:pk>', ListApplicationsResultSobesView.as_view(), name="applications-result-sobes"),
    path('sobes_result/application/<int:pk>', DetailSobesResultView.as_view(), name="sobes-result-result"),
]

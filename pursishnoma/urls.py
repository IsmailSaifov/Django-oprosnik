from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey, name='survey'),  # Главная страница с опросом
    path('submit/', views.submit_survey, name='submit_survey'),
    path('submitted/', views.submitted_view, name='submitted'),
    path('responses/', views.respons_list, name='response-list'),
    path('responses/<str:session_id>/', views.response_detail, name='response-detail'),
]

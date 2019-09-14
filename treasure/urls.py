from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('googlesignin/', views.renderLogin, name='render-login'),
    path('profile/', views.renderToken, name='render-token'),
       # path('team_register', views.team_register, name='team_register'),
    path('url/', views.getData, name='get-data-debug'),
    path('get_pin/', views.getPinCode, name='get_pin'),    
    path('create_team/', views.create_team, name='create_team'),
    path('jointeam/', views.join_team, name='join_team'),
    path('get/question_details/', views.question_details, name='question_details'),
    path('check_question_answer/', views.check_question_answer, name='check_question_answer'),
    path('team_list/', views.team_list, name='team_list'),
    path('<str:filename>', views.renderFile, name='render-file'),

    # path('teamspage/', views.teampage, name='teampage'),

]

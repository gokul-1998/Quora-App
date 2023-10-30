from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_login'), 
    path('register/', views.user_register, name='user_register'),
    path('logout/', views.user_logout, name='user_logout'), 
    path('questions/', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
]


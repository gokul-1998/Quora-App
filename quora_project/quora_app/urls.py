from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.user_login, name='user_login'), 
    path('register/', views.user_register, name='user_register'),
    path('logout/', LogoutView.as_view(next_page='user_login'),name='user_logout'), 
    path('questions/', views.question_list, name='question_list'),
    path('ask/', views.ask_question, name='ask_question'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    
]


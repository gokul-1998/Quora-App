from django import forms
from .models import Question, Answer, User
from django.contrib.auth.forms import UserCreationForm

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
from django.shortcuts import render, redirect
from .models import Question, Answer
from django.contrib.auth import login, authenticate, logout
from .forms import QuestionForm, AnswerForm, RegistrationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('question_list')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

def question_list(request):
    questions = Question.objects.all()     
    return render(request, 'question_list.html', {'questions': questions})


def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_list')
    else:
        form = QuestionForm()
    return render(request, 'ask_question.html', {'form': form})

def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_list')
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'form': form, 'question': question})


def question_detail(request, question_id):
    question = Question.objects.get(pk=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})


def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    if request.user in answer.likes.all():
        answer.likes.remove(request.user)
    else:
        answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)

# Create your views here.

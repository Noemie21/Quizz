
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Question
from django.http import HttpResponseRedirect
from django.contrib import messages
import random

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", context={"form":form})


def home(request):
    return render(request, 'questions/home.html')


def question(request, id_question):
    question = Question.objects.filter(id=id_question).get()
    questions = Question.objects.count()
    message = ""
    if(request.user):
        if request.method == 'POST':
            answer = request.POST.get('answer')
            if (answer == question.answer):
                print(questions)
                print("good answer")
                new_id_question = random.randint(1, questions)
                return redirect("/question/"+str(new_id_question))
            else:
                message = 'La réponse est fausse.'
                return HttpResponseRedirect(request.path_info)
            pass
        else:
            print(questions)
            return render(request, "questions/question.html", context={'question':question,"id_question":id_question, "messages":message})

from django.shortcuts import redirect, render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data["username"], password=form.cleaned_data["password1"])
            login(request, user)
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", context={"form": form})


@login_required
def home(request):
    current_user = request.user

    questions = Question.objects.filter(user=current_user.id)
    form = QuestionForm()
    context = {'questions': questions, 'form': form}
    return render(request, 'form/addQuestionForm.html', context)


def index(request):
    current_user = request.user

    questions = Question.objects.filter(user=current_user.id)
    form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            localForm = form.save(commit=False)
            localForm.user = request.user
            localForm.save()
        return redirect('/')
    context = {'questions': questions, 'form': form}
    return render(request, 'form/addQuestionForm.html', context)

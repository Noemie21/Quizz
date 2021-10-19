
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
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

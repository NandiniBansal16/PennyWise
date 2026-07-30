from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

from .forms import RegisterForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(request, "Account created successfully!")

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(request, "accounts/register.html", {
        "form": form
    })


def login_view(request):
    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


def profile(request):
    return render(request, "accounts/profile.html")
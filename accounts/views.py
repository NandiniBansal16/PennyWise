from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm


def register(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

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

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(request, f"Welcome back, {user.username}!")

            return redirect("dashboard")

        else:

            messages.error(request, "Invalid username or password.")

    return render(request, "accounts/login.html")


@login_required
def profile(request):
    return render(request, "accounts/profile.html")


def logout_view(request):

    logout(request)

    messages.success(request, "Logged out successfully!")

    return redirect("login")
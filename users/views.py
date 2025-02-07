from allauth.account.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from .forms import CustomSignupForm


def login_and_signup_view(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "login":
            login_form = LoginForm(data=request.POST)
            signup_form = CustomSignupForm()

            if login_form.is_valid():
                # Authenticate the user
                username = login_form.cleaned_data.get("login")  # This is the email/username field
                password = login_form.cleaned_data.get("password")
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("/")
                else:
                    messages.error(request, "Login failed. Please check your username and password.")
            else:
                messages.error(request, "Login form is invalid.")

        elif form_type == "signup":
            signup_form = CustomSignupForm(data=request.POST)
            login_form = LoginForm()

            if signup_form.is_valid():
                # Save the user
                signup_form.save(request)
                messages.success(request, "Account created successfully!")
                return redirect("/")
            else:
                messages.error(request, "Sign-up failed. Please correct the errors.")
    else:
        login_form = LoginForm()
        signup_form = CustomSignupForm()

    return render(request, "users/signin_signup.html", {"login_form": login_form, "signup_form": signup_form})


def logout_modal_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("/")
    else:
        messages.error(request, "Logout failed")
        return redirect("/")

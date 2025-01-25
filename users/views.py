from allauth.account.forms import LoginForm
from django.views import generic
from django.shortcuts import render, get_object_or_404, reverse
from .forms import CustomSignupForm

def login_and_signup_view(request):
    login_form = LoginForm()
    signup_form = CustomSignupForm()
    
    if request.method == "POST":
        if "login" in request.POST:  # Handle login form submission
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                login_form.save()
                # Redirect or handle success
        elif "signup" in request.POST:  # Handle signup form submission
            signup_form = CustomSignupForm(data=request.POST)
            if signup_form.is_valid():
                signup_form.save(request)  # Pass the request for proper signup
                # Redirect or handle success

     # Debug statement to check form instantiation
    print("Login Form:", login_form)
    print("Signup Form:", signup_form)

    context = {
        "login_form": login_form,
        "signup_form": signup_form,
    }
    return render(request, "users/signin_signup.html", context)
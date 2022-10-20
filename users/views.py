from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from users.forms import UserRegistrationForm

# Create your views here.

# 3 pathways through this
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save() # Actually put the new user into the model/db
            login(request, user)
            username = form.cleaned_data.get("username")
            messages.success(request, f"User {username} successfully created")
            return redirect("sharks-home")
    else:
        form = UserRegistrationForm()

    return render(request, "registration.html", { "form" : form})


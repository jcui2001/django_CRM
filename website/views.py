from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == "POST":
        # Retrieve the 'username' and 'password' from the 'Login' page
        # The key matches the 'name=' in the html element
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)

        # if a user has logged in the 'user' will contain information
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")

            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')


def register_user(request):
    return render(request, 'register.html', {})
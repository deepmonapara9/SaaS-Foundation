from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username =  request.POST["username"]
        password =  request.POST["password"] 
        if all([username, password]):  
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login here")
                return redirect("/")
    context = {}
    return render(request, "auth/login.html", context)

def register_view(request):
    context = {}
    return render(request, "auth/register.html", context)
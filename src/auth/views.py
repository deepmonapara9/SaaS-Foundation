from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()

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
    if request.method == "POST":
        # print(request.POST)
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        # to check the username is already in the db or not
        # username_exits = User.objects.filter(username__iexact=username).exists()
        # email_exits = User.objects.filter(email__iexact=email).exists()
        
        try:
            User.objects.create_user(username, email=email, password=password)
        except:
            pass
    context = {}
    return render(request, "auth/register.html", context)
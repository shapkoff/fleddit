from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ('There Was An Error Logging In'))
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
def register_user(request):
    user = get_user_model()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        password_repeat = request.POST["password_repeat"]

        if user.objects.filter(username=username).exists():
            messages.error(request, ("Username is already taken"))
        elif password != password_repeat:
            messages.error(request, ("Passwords don't match"))
        else:
            user.objects.create_user(username=username, password=password)
            messages.success(request, 'Successfully created')
            return redirect('login')
            
        return redirect('register')
    else:
        return render(request, 'users/register.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

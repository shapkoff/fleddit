from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from posts.models import Post

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
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')

def my_profile(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(user=request.user)
        return render(request, 'users/my_profile.html', {'posts': posts, 'username': request.user.username})

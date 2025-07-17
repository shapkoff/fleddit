from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import CreateUserForm, ChangeUserInfoForm
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
            messages.warning(request, ('There Was An Error Logging In'))
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
    if not request.user.is_authenticated:
        return redirect('login')
        
    posts = Post.objects.filter(user=request.user)

    if request.method == 'POST':
        form = ChangeUserInfoForm(request.POST, initial={'username': request.user.username, 'email': request.user.email})
        if form.is_valid():
            user = request.user
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, "User's info updated")
            return redirect('profile')
        else:
            messages.warning(request, 'Not valid info')
    else:
        form = ChangeUserInfoForm(initial={'username': request.user.username, 'email': request.user.email})

    return render(request, 'users/my_profile.html', {'posts': posts, 'username': request.user.username, 'form': form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password has changed')
            return redirect('home')
        else:
            messages.warning(request, form.errors)
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'users/change_password.html', {'form': form})

def disable_user(request):
    if request.user.is_authenticated:
        user = request.user
        user.is_active = False
        user.save()
        messages.success(request, 'User is deleted')
    return redirect('home')

def user_profile(request, id):
    user = get_user_model().objects.get(id=id)
    posts = Post.objects.filter(user=user)
    return render(request, 'users/user_profile.html', {'user': user, 'posts': posts})

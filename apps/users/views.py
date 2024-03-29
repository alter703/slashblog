from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from apps.blog.models import Post


# Create your views here.

def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:index')

    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    form = UserCreationForm()
    if request.method == 'POST':  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            user = form.save()
            login(request, user)
            return redirect('main:index')
        
    return render(request, 'users/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('main:index')


@login_required
def profile_view(request):
    posts = Post.objects.filter(author=request.user)

    context = {
        'posts': posts,
    }
    return render(request, 'users/profile.html', context)
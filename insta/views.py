

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# from .models import Post, Comment, Profile, Follow
# from .forms import SignUpForm, UpdateUserForm, UpdateUserProfileForm, PostForm, CommentForm
from django.contrib.auth import login, authenticate
# from django.template.loader import render_to_string
from django.contrib.auth.models import User



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def index(request):
    
    return render(request, 'insta/index.html', )


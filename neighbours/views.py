from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, PostForm, ProfileForm, CommentForm
from .models import Post, Profile, Comments
from  django.contrib import messages
# from .emails import send_activation_email
# from .tokens import account_activation_token
# Create your views here.

def home(request):
    return render(request,'home.html')
@login_required(login_url='/accounts/login')
def index(request):
    posts = Post.get_all_posts()

    return render(request, 'index.html',{'posts':posts})
@login_required(login_url='/accounts/login')
def kampala(request):
    posts = Post.get_all_posts()

    return render(request, 'Nairobi.html',{'posts':posts})

@login_required(login_url='/accounts/login')
def capetown(request):
    posts = Post.get_all_posts()

    return render(request, 'london.html',{'posts':posts})

def signup(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                send_activation_email(user, current_site, to_email)
                return HttpResponse('Confirm your email address to complete registration')
        else:
            form = SignupForm()
            return render(request, 'registration/signup.html',{'form':form})


def profile(request,username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    
    posts = Post.get_profile_posts(profile.id)
    title = f'@{profile.username} Hood Updates'

    return render(request, 'profile/profile.html',{'title':title, 'profile':profile,'profile_details':profile_details,'posts':posts})
@login_required(login_url='/accounts/login')
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.profile = request.user
            # print(f'post is {upload.post}')
            upload.save()
            return redirect('profile', username=request.user)
    else:
        form = PostForm()
    
    return render(request, 'profile/upload_post.html', {'form':form})

@login_required(login_url='/accounts/login')
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile.html')
    else:
        form = ProfileForm()

    return render(request, 'profile/edit_profile.html', {'form':form})


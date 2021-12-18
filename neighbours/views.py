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
    
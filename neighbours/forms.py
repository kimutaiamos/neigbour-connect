from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile, Comments
from pyuploadcare.dj.forms import FileWidget
from pyuploadcare.dj.models import ImageField

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text = 'Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['likes', 'post_date', 'profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['post', 'user']
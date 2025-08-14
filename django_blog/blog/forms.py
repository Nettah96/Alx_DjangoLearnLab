from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags in the form
        widgets = {
            'tags': TagWidget(),  
        }

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Separate tags with commas")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()


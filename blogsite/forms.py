from django.test import TestCase
from .models import Post
from django import forms
# Create your tests here.
class PostForm(forms.ModelForm):
    class Meta :
        model = Post
        fields = "__all__"
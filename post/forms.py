from django import forms
from .models import Post

class AddPostForm(forms.Form):
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_date']
        
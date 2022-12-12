from django import forms
from .models import Post

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    Due_To = forms.DateField()
    class Meta:
        model = Post
        fields = ['title', 'description', 'created_date']
        
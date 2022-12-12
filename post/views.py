from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Post as Task

def addPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        Post = Task.objects.all()
    return render(request, 'post/addPost.html')

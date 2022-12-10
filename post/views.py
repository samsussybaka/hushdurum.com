from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm

def addPost(request):
    form = AddPostForm()
    return render(request, 'post/addPost.html', {'form': form})

    


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import AddPostForm
from .models import Post as Task

def addPost(request):
    form = AddPostForm(request.POST)
    if request.method == 'POST':
        Post = Task.objects.all()
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
    context = {
        'form': form,
    }
    return render(request, 'post/addPost.html', context)



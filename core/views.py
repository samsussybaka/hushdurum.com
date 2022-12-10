from django.shortcuts import render, get_object_or_404
from post.models import Post as Task

# Create your views here.

def frontpage(request):
    Post = Task.objects.all()
    return render(request, 'core/home.html', {'Post': Post})

def PostPage(request):
    return render(request, 'core/base.html')

def CoolPage(request):
    return render(request, 'core/cool.html')

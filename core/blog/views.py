from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, template_name='blog/index.html', context={'posts': posts})

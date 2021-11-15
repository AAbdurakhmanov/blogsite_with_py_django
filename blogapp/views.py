from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogapp/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()


    context = {'post': post, 'form': form}
    return render(request, 'blogapp/post_detail.html', context)


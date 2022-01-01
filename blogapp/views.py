from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Post
from .forms import CommentForm
# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogapp/index.html', context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = CommentForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blogapp/post_detail.html', {'post': post, 'form': form})

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AddPostView(CreateView):
    model = Post
    template_name = 'blogapp/add_post.html'
    success_url = reverse_lazy('home')
    fields = '__all__'

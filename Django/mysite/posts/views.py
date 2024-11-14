from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
def homePage(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'posts/homepage.html', { 'posts' : posts})


def post_page(request, id):
    post = Post.objects.get(slug = id)
    return render(request, 'posts/post_page.html', {'post' : post})

@login_required(login_url="/users/login/")
def new_post(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            return redirect("posts:homepage")
    else:
        form = forms.CreatePost()
    return render(request, "posts/new_post.html", {'form':form})
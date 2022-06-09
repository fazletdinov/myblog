from django.shortcuts import render, get_object_or_404
from .models import Post, PublishedManager

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status='опубликован', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


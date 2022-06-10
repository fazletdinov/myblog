from django.shortcuts import render, get_object_or_404
from .models import Post, PublishedManager
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

#def post_list(request):
#    object_list = Post.published.all()
#    paginator = Paginator(object_list, 3) # По 3 статьи на каждой странице
#    page = request.GET.get('page')
#    try:
#        posts = paginator.page(page)
#    except PageNotAnInteger:
#        # Если страница не является целым числом, возращаем первую страницу
#        posts = paginator.page(1)
#    except EmptyPage:
#        # Если номер страницы больше, чем общее количество страниц, возращаем последнюю.
#        posts = paginator.page(paginator.num_pages)
#    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post, slug=post_slug, status='опубликован', publish__year=year,
                             publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})


from django.shortcuts import render, get_object_or_404
from .models import Post, PublishedManager
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

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

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status="опубликован")
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) рекомендует вам прочитать"' \
                      '{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Читать "{}" по ссылке {}\n\n{}\'s комментарии:' \
                      '{}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'testusert022@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html', {'post': post, 'form': form,
                                                            'sent': sent})




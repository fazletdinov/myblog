from django.urls import path
from . import views
from .feeds import LatestPostFeed
from django.views.decorators.csrf import csrf_exempt

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/',
         views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('feed/', LatestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
    path('create/', views.create, name='post_create'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
]
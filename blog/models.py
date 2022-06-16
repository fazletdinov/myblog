from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='опубликован')

class Post(models.Model):
    STATUS_CHOICES = (
        ('неопубликован', 'Неопубликован'),
        ('опубликован', 'Опубликован')
    )
    title = models.CharField('Заголовок', max_length=250)
    slug = models.SlugField('URL', max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts',
                               verbose_name="Автор")
    body = models.TextField('Текст')
    publish = models.DateTimeField('Дата публикации', default=timezone.now)
    created = models.DateTimeField('Дата создания статьи', auto_now_add=True)
    updated = models.DateTimeField('Дата изменения', auto_now=True)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='неопубликован')
    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishedManager() # Собственный менеджер
    tags = TaggableManager('Теги')

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'year': self.publish.year, 'month': self.publish.month,
                                                   'day': self.publish.day, 'post_slug': self.slug})
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    name = models.CharField('Имя', max_length=80)
    email = models.EmailField('Адрес электройнной почты')
    body = models.TextField('Текст')
    created = models.DateTimeField('Дата написания', auto_now_add=True)
    update = models.DateTimeField('Дата обноавления', auto_now=True)
    active = models.BooleanField('Статус', default=True)

    class Meta:
        ordering = ('created',)
        verbose_name = 'Комментарий'
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return f'Комментарций {self.name} к {self.post}'


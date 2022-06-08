from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
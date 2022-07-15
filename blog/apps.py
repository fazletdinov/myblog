from django.apps import AppConfig
from django.utils.deprecation import MiddlewareMixin

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'
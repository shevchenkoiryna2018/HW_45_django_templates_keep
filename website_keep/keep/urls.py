from django.urls import path
from . import views

app_name = 'keep'

urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('archives', views.archives, name='archives'),
    path('blog', views.blog, name='blog'),
    path('blog/single', views.blog_single, name='blog_single'),
    path('page', views.page, name='page'),
]


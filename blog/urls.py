from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('blog/', views.blog, name='blog-blog'),
    path('about/', views.about, name='blog-about'),
    path('blogs/<str:id>', views.read_more, name='blog-read_more'),
    path('notice/', views.notice, name='notice'),
]

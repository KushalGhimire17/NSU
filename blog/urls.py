from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    # path('blog/', views.blog, name='blog-blog'),
    path('about/', views.about, name='blog-about'),
    path('blogs/<str:id>', views.read_more, name='blog-read_more'),
    path('notice/', views.notice, name='notice'),

    path('blog/', views.dashboard, name='dashboard'),
    path('blog/<int:id>', views.dashboard, name='post_update'),
    path('blog/post_list/', views.post_list, name='post_list'),
]

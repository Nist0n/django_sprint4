﻿from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',
         views.category_posts,
         name='category_posts'),
    path('profile/<str:username>/',
         views.profile_view,
         name='profile'),
    path('posts/create/',
         views.PostCreateView.as_view(),
         name='post_create'),
    path('posts/<int:post_id>/edit/',
         views.PostUpdateView.as_view(),
         name='post_edit'),
    path('posts/<int:post_id>/delete/',
         views.PostDeleteView.as_view(),
         name='post_delete'),
    path('posts/<int:post_id>/comment/',
         views.add_comment,
         name='add_comment'),
    path('posts/<int:post_id>/edit_comment/<int:comment_id>/',
         views.edit_comment,
         name='edit_comment'),
    path('posts/<int:post_id>/delete_comment/<int:comment_id>/',
         views.delete_comment,
         name='delete_comment'),
]

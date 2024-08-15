from django.urls import path
from .views import PostListView, PostDetailView, PostSearchView, create_news

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('news/search/', PostSearchView.as_view(), name='post_search'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create/', create_news, name='post_create'),
]

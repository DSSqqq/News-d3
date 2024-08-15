from django.urls import path
from .views import PostListView, PostDetailView, PostSearchView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('news/search/', PostSearchView.as_view(), name='post_search'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('news/create/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

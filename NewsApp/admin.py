from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')
    search_fields = ('authorUser__username',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'categoryType', 'dateCreation', 'rating')
    list_filter = ('author', 'categoryType')
    search_fields = ('title', 'author__authorUser__username')
    # Убрать filter_horizontal
    # filter_horizontal = ('postCategory',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('commentUser', 'commentPost', 'dateCreation', 'rating')
    list_filter = ('commentUser', 'commentPost')
    search_fields = ('commentUser__username', 'commentPost__title')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment, CommentAdmin)
from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, DateFilter
from .models import Post, Category

class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        field_name='postCategory',
        label='Категория',


    )

    title = CharFilter(field_name='title', lookup_expr='icontains', label='Название')

    date_from = DateFilter(
        field_name='dateCreation',
        lookup_expr='lt',
        label='Позже даты',
        widget=forms.DateInput(attrs={'type': 'date'})  # Включаем HTML5 виджет для выбора даты
    )
    class Meta:
        model = Post
        fields = ['title', 'category','date_from']
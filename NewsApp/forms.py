from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'categoryType', 'postCategory']  # Используем существующие поля
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            'categoryType': forms.Select(attrs={'class': 'form-control'}),
            'postCategory': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'author': forms.HiddenInput(),  # Прятать поле автор (если оно должно быть установлено программно)
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст статьи',
            'categoryType': 'Тип публикации',
            'postCategory': 'Категория',
            'author': 'Автор',
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Заголовок должен содержать как минимум 5 символов.")
        return title

    def clean_text(self):
        text = self.cleaned_data.get('text')
        if len(text) < 20:
            raise forms.ValidationError("Текст статьи должен содержать не менее 20 символов.")
        return text
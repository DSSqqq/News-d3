from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

# считаем суммарный рейтинг
    def update_rating(self):
        # применяем функцию сум к полю рейтинг и он складывает к модели пост связанную с этим автором
        PostRat = self.post_set.aggregate(postRating=Sum('rating'))
        # получаем значения
        pRat = 0
        pRat += PostRat.get('postRating')

        # Делаем тоже для коментов
        # сначала обращаемся к authorUser
        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        # получаем значения
        cRat = 0
        cRat += commentRat.get('commentRating')

        # складываем
        self.ratingAuthor = pRat *3 + cRat
        # Сохраняем
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return self.name

from django.db import models

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    # Поле выбора категории
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=NEWS)
    # Дата создания
    dateCreation = models.DateTimeField(auto_now_add=True)
    # Связное поле с категорией
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    # Заголовок
    title = models.CharField(max_length=128)
    # Текст статьи
    text = models.TextField()
    # Рейтинг
    rating = models.SmallIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    # Метод для получения превью текста
    def preview(self):
        return self.text[:20] + '...'

    # Метод для подсчета рейтинга
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    class Meta:
        ordering = ['-dateCreation']  # Сортировка от более свежих к старым

# этот метод берет с поста первые 123 символа и в конце ставит многоточие
    def preview(self):
        return self.text[0:123] + '...'

# Промежуточная модель
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Даем возможность комментировать всем юзерам
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    # Не ограничиваем кол-во символов
    text = models.TextField()
    # Авто-дата
    dateCreation = models.DateTimeField(auto_now_add=True)
    # Рейтинг
    rating = models.SmallIntegerField(default=0)

    # Прибавляем либо отнимаем 1 в поле рейтинга
    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
from django.db import models
from users.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название Категории')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название Жанра')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):

    name = models.CharField(max_length=256, verbose_name='Название')
    year = models.IntegerField(verbose_name='Год выхода')
    description = models.TextField(
        max_length=256,
        verbose_name='Описание',
        blank=True,
        null=True,
    )

    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        through_fields=('title', 'genre')
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return (f'{self.title} - {self.genre}')


class Review(models.Model):
    title_id = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )
    text = models.TextField(
        verbose_name='Текст рецензии'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор рецензии'
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации рецензии'
    )

    def __str__(self):
        return self.text[:30]


class Comment(models.Model):
    review_id = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Рецензия'
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации комментария'
    )

    def __str__(self):
        return self.text[:30]

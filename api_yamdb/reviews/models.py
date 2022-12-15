from django.db import models

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

    name = models.CharField(max_length=256, verbose_name='Название фильма')
    year = models.IntegerField(verbose_name='Год выхода')
    description = models.CharField(
        max_length=256,
        verbose_name='Описание фильма',
        blank=True,
        null=True,
    )

    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        through_fields=('title', 'genre')
    )

    categoty = models.ForeignKey(
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
        return self.title, self.genre

import uuid

from django.db import models


# Create your models here.

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    title = models.CharField(max_length=1000, verbose_name='Book title')
    creation_date = models.DateField(blank=True, null=True, verbose_name='Date of creation')
    description = models.TextField(max_length=100000, verbose_name="Book description")
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE)
    genre = models.ManyToManyField('Genre', through='BookGenre')

    class Meta:
        verbose_name = 'Book'
        db_table = 'book'
        ordering = ['title']

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1000, verbose_name='Person`s name')

    class Meta:
        verbose_name = 'Author'
        db_table = 'author'
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=1000, verbose_name='Genre')

    class Meta:
        verbose_name = 'Genre'
        db_table = 'genre'
        ordering = ['name']

    def __str__(self):
        return self.name


class BookGenre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    book = models.ForeignKey('Book', default=None, null=True, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'genre_book'
        unique_together = (('book', 'genre'),)

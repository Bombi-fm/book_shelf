from django.contrib import admin
from .models import Book, Author, Genre, BookGenre


# Register your models here.

class BookInLine(admin.TabularInline):
    model = Book


class BookGenreInLine(admin.TabularInline):
    model = BookGenre
    extra = 0
    can_delete = False


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'id')
    inlines = (BookGenreInLine,)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
    inlines = (BookInLine, )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
    inlines = (BookGenreInLine, )

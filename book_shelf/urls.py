
from django.contrib import admin
from django.urls import path
from bookshelf.views import BookListView, BookDetailView, GenreListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookListView.as_view(), name='books'),
    path('books/<str:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('genres/', GenreListView.as_view(), name='genres'),

]

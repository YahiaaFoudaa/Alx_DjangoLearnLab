from django.urls import path
from .views import BookListView, BookCreateView, BookDeleteView, BookDetailView, BookUpdateView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/', BookCreateView.as_view(), name='book-create'),
    path('books/', BookDeleteView.as_view(), name='book-delete'),
    path('books/', BookDetailView.as_view(), name='book-detail'),
    path('books/', BookCreateView.as_view(), name='book-Create'),
    path('books/', BookUpdateView.as_view(), name='book-update'),
]
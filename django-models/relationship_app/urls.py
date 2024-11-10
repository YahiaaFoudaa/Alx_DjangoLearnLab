from django.urls import path
from .views import list_books
from .views import LibraryDetailView 
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import register
from . import views

urlpatterns = [
    path('library/', LibraryDetailView.as_view(), name='library-detail'),
    path('list_books/', list_books, name='list_books'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.registeregister.as_view(), name='register'),
]
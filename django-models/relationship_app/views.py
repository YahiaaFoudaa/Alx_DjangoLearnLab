from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all() 
    context = {'book_list': books} 
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context['book'] = self.object.books.all()
        return context
    
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

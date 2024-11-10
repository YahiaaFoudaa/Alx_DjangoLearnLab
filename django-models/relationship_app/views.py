from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from .models import Book 
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User

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
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # This view is only accessible to users with the 'Admin' role
    return render(request, 'relationship_app/admin_view.html')  # You can customize the template as needed

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    # This view is only accessible to users with the 'Librarian' role
    return render(request, 'relationship_app/librarian_view.html')  # Customize the template as needed

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    # This view is only accessible to users with the 'Member' role
    return render(request, 'relationship_app/member_view.html')  # Customize the template as needed

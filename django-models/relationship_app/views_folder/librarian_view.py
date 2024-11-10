# views/librarian_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if the user has the 'Librarian' role
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
def librarian_view(request):
    # This view is only accessible to users with the 'Librarian' role
    return render(request, 'librarian_view.html')  # Customize the template as needed

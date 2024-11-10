# views/admin_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if the user has the 'Admin' role
def is_admin(user):
    return user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
def admin_view(request):
    # This view is only accessible to users with the 'Admin' role
    return render(request, 'admin_view.html')  # You can customize the template as needed

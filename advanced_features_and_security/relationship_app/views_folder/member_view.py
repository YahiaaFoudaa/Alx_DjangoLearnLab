# views/member_view.py
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if the user has the 'Member' role
def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_member)
def member_view(request):
    # This view is only accessible to users with the 'Member' role
    return render(request, 'member_view.html')  # Customize the template as needed

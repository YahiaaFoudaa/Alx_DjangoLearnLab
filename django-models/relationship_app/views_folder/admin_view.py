from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

@login_required
def admin_view(request):
    # Check if the user has the 'Admin' role
    if request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You do not have permission to view this page.")
    
    # Proceed to render the page for Admin users
    return render(request, 'admin_view.html')
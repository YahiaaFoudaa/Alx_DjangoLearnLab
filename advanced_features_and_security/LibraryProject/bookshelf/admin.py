from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

class CustomerUserAdmin(UserAdmin):
    list_display = ('email', 'date_of_birth', 'profile_photo', 'is_admin')
    list_filter = ('is_admin', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    search_fields = ('email', 'date_of_birth')
    ordering = ('email',)
    
admin.site.register(Book, BookAdmin,CustomerUserAdmin)
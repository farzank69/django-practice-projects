from django.contrib import admin
from . models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)  # Make the slug field read-only in the admin interface
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title field in the admin interface
    list_filter = ('author', 'rating') # Add filters for author and rating in the admin list view
    list_display = ('title', 'author') # Display title and author in the admin list view
admin.site.register(Book, BookAdmin)
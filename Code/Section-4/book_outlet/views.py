from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg
from .models import Book
# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-title') # Fetch all books from the database and order them by title in descending order   
    num_book = books.count() 
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, "book_outlet/index.html", {
        'books': books,
        'total_number_of_books': num_book,
        'average_rating': avg_rating
        })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    # Or use get_object_or_404 shortcut to do the same thing
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': book.title, 
        'author': book.author,
        'rating': book.rating,
        'is_bestseller': book.is_bestselling
    })
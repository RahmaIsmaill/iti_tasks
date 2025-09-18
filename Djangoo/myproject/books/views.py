from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Author

def home(request):
    return render(request, "books/home.html")

def book_detail(request):
    return render(request, "books/book_detail.html")

def about(request):
    return render(request, "books/about.html")

def contact(request):
    return render(request, "books/contact.html")

# 1. List Books
def books_list(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {"books": books, "title": "Books List"})

# 2. Add Book
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        
        author = get_object_or_404(Author, pk=author_id)
        
        Book.objects.create(title=title, author=author)
        return redirect('books_list')
    
    authors = Author.objects.all()
    return render(request, 'books/add_book.html', {'authors': authors, 'title': 'Add Book'})

# 3. Edit Book
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = get_object_or_404(Author, pk=author_id)
        
        book.save()
        return redirect('books_list')
    
    authors = Author.objects.all()
    return render(request, 'books/edit_book.html', {'book': book, 'authors': authors, 'title': 'Edit Book'})

# 4. Delete Book
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('books_list')
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from .forms import BookForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# ---------- Books API ----------
@api_view(['GET', 'POST'])
def book_list_api(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_api(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- Authors API ----------
@api_view(['GET', 'POST'])
def author_list_api(request):
    if request.method == 'GET':
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def author_detail_api(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- HTML Views ----------
def index(request):
    return render(request, 'books/index.html')


def list_books(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})


def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})


def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'books/delete_confirm.html', {'book': book})


def fantasy_books(request):
    books = Book.objects.filter(genre='fantasy')
    return render(request, 'books/fantasy.html', {'books': books})


def scifi_books(request):
    books = Book.objects.filter(genre='scifi')
    return render(request, 'books/scifi.html', {'books': books})


def mystery_books(request):
    books = Book.objects.filter(genre='mystery')
    return render(request, 'books/mystery.html', {'books': books})


def fiction_books(request):
    books = Book.objects.filter(genre='fiction')
    return render(request, 'books/fiction.html', {'books': books})

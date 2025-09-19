from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('home/', views.index, name='home'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('fantasy/', views.fantasy_books, name='fantasy_books'),
    path('scifi/', views.scifi_books, name='scifi_books'),
    path('mystery/', views.mystery_books, name='mystery_books'),
    path('fiction/', views.fiction_books, name='fiction_books'),

    path('<int:pk>/', views.book_detail, name='book_detail'),

    # API endpoints
    path('api/books/', views.book_list_api, name='book_list_api'),
    path('api/books/<int:pk>/', views.book_detail_api, name='book_detail_api'),
    path('api/authors/', views.author_list_api, name='author_list_api'),
    path('api/authors/<int:pk>/', views.author_detail_api, name='author_detail_api'),
]

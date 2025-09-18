from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.books_list, name='books_list'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('detail/<int:book_id>/', views.book_detail, name='book_detail'),  # FIXED
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
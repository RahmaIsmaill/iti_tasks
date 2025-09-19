from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)  # allow NULL


    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = [
        ('fantasy', 'Fantasy'),
        ('scifi', 'Science Fiction'),
        ('mystery', 'Mystery'),
        ('fiction', 'Fiction'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES,
        default='fiction'  
    )

    def __str__(self):
        return f"{self.title} by {self.author.name}"

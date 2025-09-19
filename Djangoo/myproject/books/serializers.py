from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']


from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre']

    def create(self, validated_data):
        # Handle author by name on create
        author_name = validated_data.pop("author")
        author, _ = Author.objects.get_or_create(name=author_name)
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        # Handle author by name on update
        author_name = validated_data.pop("author", None)
        if author_name:
            author, _ = Author.objects.get_or_create(name=author_name)
            instance.author = author

        instance.title = validated_data.get("title", instance.title)
        instance.genre = validated_data.get("genre", instance.genre)
        instance.save()
        return instance


from rest_framework import serializers
from .models import Author, Book

class BookSerializerPK(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'price']

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializerPK(many = True, read_only = True)
    class Meta:
        model = Author
        fields = ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author', None)

        if author_data is not None:
            author, created = Author.objects.get_or_create(**author_data)
        
        book = Book.objects.create(author = author, **validated_data)

        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.price = validated_data.get('price', instance.price)
        author_data = validated_data.pop('author', None)

        if author_data is not None:
            author, created = Author.objects.get_or_create(**author_data)
            instance.author = author
        instance.save()
        return instance


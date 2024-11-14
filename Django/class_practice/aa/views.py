from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.response import Response

class BookView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            books = Book.objects.all()
            serializer = BookSerializer(books, many = True)
            return Response(serializer.data)
        else:
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        
    def put(self, request, id=None, *args, **kwargs):
        book = Book.objects.get(pk=id)
        data = request.data 
        serializer = BookSerializer(book, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'object updated successfully'})
        else:
            return Response(serializer.errors)
        

    def delete(self, request, id=None, *args, **kwargs):
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return Response({'error' : 'Book not found'})

        book.delete()
        return Response({'message' : 'Book deleted successfully'})

    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'object created successfully'})
        else:
            return Response(serializer.errors)
        


class AuthorView(APIView):
    def get(self, request, id=None, *args, **kwargs):
        if id is None:
            authors = Author.objects.all()
            serializer = AuthorSerializer(authors, many=True)
            return Response(serializer.data)
        else:
            author = Author.objects.get(pk=id)
            serializer = AuthorSerializer(author)
            return Response(serializer.data)
        
    def put(self, request, id=None, *args, **kwargs):
        author = Author.objects.get(pk=id)
        data = request.data 
        serializer = AuthorSerializer(author, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'object updated successfully'})
        else:
            return Response(serializer.errors)
        

    def delete(self, request, id=None, *args, **kwargs):
        try:
            author = Author.objects.get(pk=id)
        except Author.DoesNotExist:
            return Response({'error' : 'author not found'})

        author.delete()
        return Response({'message' : 'author deleted successfully'})

    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = AuthorSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'object created successfully'})
        else:
            return Response(serializer.errors)
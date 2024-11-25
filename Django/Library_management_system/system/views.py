from django.shortcuts import render
from .models import Book, Author, Member, BorrowRecord
from .serializers import BookSerializer, AuthorSerailizer, MemberSerializer, AuthorBooksSerializer, BookRecordSerializer, BorrowedByMemberSerializer, MemberWhoBorrowedABookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.utils import timezone


class AuthorView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = AuthorSerailizer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "Author created successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id = None, *args, **kwargs):
        if id is not None:
            try:
                author = Author.objects.get(id = id)
            except Author.DoesNotExist as e:
                return Response(
                    {
                        "error" : "Author not found"
                    },
                    status= status.HTTP_404_NOT_FOUND
                )
            serializer = AuthorSerailizer(author)
            return Response(
                {
                    "data" : serializer.data
                },
                status= status.HTTP_200_OK
            )
        else:
            authors = Author.objects.all()
            serializer = AuthorSerailizer(authors, many = True)
            return Response(
                {
                    "data" : serializer.data
                },
                status= status.HTTP_200_OK
            )



    def delete(self, request, id, *args, **kwargs):
        try:
            author = Author.objects.get(id = id)
        except Author.DoesNotExist as e:
            return Response(
                {
                    "error" : "Author not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        try:
            author.delete()
            return Response(
                {
                    "message" : "Author deleted successfully"
                }, 
                status= status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error" : "Failed to delete author"
                },
                status= status.HTTP_405_METHOD_NOT_ALLOWED
            )
        

    def put(self, request, id, *args, **kwargs):
        try:
            author = Author.objects.get(id = id)
        except Author.DoesNotExist as e:
            return Response(
                {
                    "error" : "Author not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        serializer = AuthorSerailizer(data = data, instance = author)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "Author modified successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = BookSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "Book created successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    


    def get(self, request, id = None, *args, **kwargs):
        if id is not None:
            try:
                book = Book.objects.get(id = id)
            except Book.DoesNotExist as e:
                return Response(
                    {
                        "error" : "Book not found"
                    },
                    status= status.HTTP_404_NOT_FOUND
                )
            serializer = BookSerializer(book)
            return Response(
                {
                    "data" : serializer.data
                },
                status= status.HTTP_200_OK
            )
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many = True)
            return Response(
                {
                    "data" : serializer.data
                },
                status= status.HTTP_200_OK
            )



    def delete(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id = id)
        except Book.DoesNotExist as e:
            return Response(
                {
                    "error" : "Book not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        try:
            book.delete()
            return Response(
                {
                    "message" : "Book deleted successfully"
                }, 
                status= status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error" : "Failed to delete Book"
                },
                status= status.HTTP_405_METHOD_NOT_ALLOWED
            )
        

    def put(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id = id)
        except Book.DoesNotExist as e:
            return Response(
                {
                    "error" : "Book not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        serializer = BookSerializer(data = data, instance = book)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "Book modified successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)



class MembersView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data 
        serializer = MemberSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "Member created successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, *args, **kwargs):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many = True)
        return Response(
            {
                "data" : serializer.data
            },
            status= status.HTTP_200_OK
)

class MemberView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            member = Member.objects.get(id = id)
        except Member.DoesNotExist as e:
            return Response(
                {
                    "error" : "member not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        serializer = MemberSerializer(member)
        return Response(
            {
                "data" : serializer.data
            },
            status= status.HTTP_200_OK
        )
    def delete(self, request, id, *args, **kwargs):
        try:
            member = Member.objects.get(id = id)
        except Member.DoesNotExist as e:
            return Response(
                {
                    "error" : "member not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        try:
            member.delete()
            return Response(
                {
                    "message" : "member deleted successfully"
                }, 
                status= status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "error" : "Failed to delete member"
                },
                status= status.HTTP_405_METHOD_NOT_ALLOWED
            )
        

    def put(self, request, id, *args, **kwargs):
        try:
            member = Member.objects.get(id = id)
        except Member.DoesNotExist as e:
            return Response(
                {
                    "error" : "member not found"
                },
                status= status.HTTP_404_NOT_FOUND
            )
        
        data = request.data
        serializer = MemberSerializer(data = data, instance = member)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message" : "member modified successfully",
                    "data" : serializer.data 
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                "error" : serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)



class AuthorBook(APIView):
    def get(self, request, id, *args, **kwargs):
        author = Author.objects.get(id = id)
        serializer = AuthorBooksSerializer(instance = author)
        return Response(serializer.data)
    
class BookByGenre(APIView):
    def get(self, request, genre, *args, **kwargs):
        books = Book.objects.filter(genre = genre)
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
class BorrowBookView(APIView):
    def post(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id = id)
            if book.status == 'borrowed':
                return Response({
                    "message" : "Book not available"
                },
                status=status.HTTP_200_OK)
            else:
                data = request.data
                record_serializer = BookRecordSerializer(data = data)

                if record_serializer.is_valid():
                    record_serializer.save()
                    book.status = "borrowed"
                    book.save()
                    return Response(
                        {
                            "message" : "Book borrowed successfully"
                        }
                    )
                else:
                    return Response(record_serializer.errors)
        except Book.DoesNotExist:
            return Response(
                {
                    "error" : "Book not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
class ListBorrowRecords(ListAPIView):
    queryset = BorrowRecord.objects.all()
    serializer_class = BookRecordSerializer


class ReturnBookView(APIView):
    def put(self, request, *args, **kwargs):
        book_id = request.query_params.get("book_id", None)
        member_id = request.query_params.get("member_id", None)
        try:
            record = BorrowRecord.objects.get(book = book_id,
                                          member = member_id,
                                          return_date__isnull = True)
            record.return_date = timezone.now().date()
            record.save()

            book = Book.objects.get(id = book_id)
            book.status = "available"
            book.save()

            return Response(
                {
                    "message" : "Book returned successfully"
                }
            )
        except BorrowRecord.DoesNotExist:
            return Response(
                {
                    "error" : "Record not found"
                }
            )


class BooksBorrowedByMember(APIView):
    def get(self, request, id, *args, **kwargs):
        books_borrowed = BorrowRecord.objects.filter(member = id, return_date__isnull = True)
        serializer = BorrowedByMemberSerializer(books_borrowed, many = True)
        return Response(serializer.data)


class MemberWhoBorrowedABookView(APIView):
    def get(self, request, id, *args, **kwargs):
        borrow_records = BorrowRecord.objects.filter(book = id)
        serializer = MemberWhoBorrowedABookSerializer(borrow_records, many = True)
        return Response(serializer.data)
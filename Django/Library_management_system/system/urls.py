from django.contrib import admin
from django.urls import path, include
from .views import AuthorView, BookView, MembersView, MemberView, AuthorBook, BookByGenre, BorrowBookView, ListBorrowRecords, ReturnBookView, BooksBorrowedByMember, MemberWhoBorrowedABookView

urlpatterns = [
    path("author/", AuthorView.as_view(), name="authors-view"),
    path("author/<int:id>", AuthorView.as_view(), name="author-view"),
    path("author/<int:id>/books", AuthorBook.as_view(), name="author-books"),
    path("member/", MembersView.as_view(), name="members-view"),
    path("member/<int:id>", MemberView.as_view(), name="member-view"),
    path("book/", BookView.as_view(), name="books-view"),
    path("book/<int:id>", BookView.as_view(), name="book-view"),
    path("books/filter/genre/<str:genre>", BookByGenre.as_view(), name="filter-genre"),
    path("book/borrow/<int:id>", BorrowBookView.as_view(), name="borrow-book"),
    path("bookrecord/list", ListBorrowRecords.as_view(), name="list-record"),
    path("return_book/", ReturnBookView.as_view(), name="return-book"),
    path("member/<int:id>/borrowed_books", BooksBorrowedByMember.as_view(), name="borrowed-books"),
    path("book/<int:id>/members", MemberWhoBorrowedABookView.as_view(), name="member-borrowed-books"),

]

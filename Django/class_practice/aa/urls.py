
from django.contrib import admin
from django.urls import path, include
from .views import BookView, AuthorView

urlpatterns = [
    path("list/", BookView.as_view(), name = "list-book"),
    path("retrieve/<int:pk>", BookView.as_view(), name = "retrieve-book"),
    path("update/<int:pk>", BookView.as_view(), name = "update-book"),
    path("delete/<int:pk>", BookView.as_view(), name = "delete-book"),
    path("create/", BookView.as_view(), name = "create-book"),
    path("list_author/", AuthorView.as_view(), name = "list_author"),
    path("retrieve_author/<int:pk>", AuthorView.as_view(), name = "retrieve_author"),
    path("update_author/<int:pk>", AuthorView.as_view(), name = "update_author"),
    path("delete_author/<int:pk>", AuthorView.as_view(), name = "delete_author"),
    path("create_author/", AuthorView.as_view(), name = "create_author"),
]

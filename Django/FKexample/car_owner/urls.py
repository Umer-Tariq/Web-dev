from django.urls import path, include
from . import views


urlpatterns = [
    path("add_owner/", views.add_owner, name="add-owner"),
    path("update_owner/<int:pk>", views.update_owner, name="update-owner"),
    path("list_owner/", views.list_owner, name="list-owner"),
    path("add_car/", views.add_car, name="add-car"),
    path("update_car/<int:pk>", views.update_car, name="update-car"),
    path("list_car/", views.list_car, name="list-car"),
    path("owner_car/<int:pk>", views.owner_car, name="owner-car"),
]
